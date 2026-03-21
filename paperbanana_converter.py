import json
import re
from dataclasses import dataclass
from typing import Any, Dict, List


STYLE_MAP = {
    "photorealistic": "photorealistic, publication-ready rendering",
    "realistic": "realistic, publication-ready rendering",
    "hyper realistic": "ultra-detailed realistic rendering",
    "cinematic": "cinematic composition with strong storytelling",
    "digital art": "clean digital illustration, publication-ready quality",
    "oil painting": "painterly oil-texture style with academic polish",
    "anime": "high-quality anime illustration with clean line art",
    "cartoon": "clean vector-like cartoon style with clear silhouette",
    "watercolor": "soft watercolor texture with controlled contrast",
    "isometric": "isometric infographic style with clear geometry",
    "scientific diagram": "scientific diagram style, clear labels, high readability",
    "flat design": "flat design infographic style with strong hierarchy",
}

QUALITY_MAP = {
    "best quality": "ultra clear details",
    "masterpiece": "high aesthetic quality",
    "8k": "high-resolution details",
    "highly detailed": "fine-grained texture and structure",
    "ultra detailed": "fine-grained texture and structure",
    "sharp focus": "crisp edges and clear focal emphasis",
}

COMPOSITION_MAP = {
    "close-up": "close-up framing on the main subject",
    "wide shot": "wide composition with spatial context",
    "low angle": "low-angle perspective for visual impact",
    "top view": "top-down composition with clear layout",
    "symmetrical": "symmetrical composition with visual balance",
    "rule of thirds": "rule-of-thirds composition with clear focal point",
}

COLOR_MAP = {
    "vibrant": "vibrant but controlled color palette",
    "muted": "muted color palette with soft contrast",
    "monochrome": "monochrome palette with tonal depth",
    "blue and orange": "cinematic teal-orange color contrast",
    "warm tones": "warm color temperature with soft highlights",
    "cool tones": "cool color temperature with clean atmosphere",
}

STYLE_MAP_ACADEMIC = {
    "scientific diagram": "scientific diagram style, clear labels, high readability, publication-ready",
    "flowchart": "methodology flowchart, flat schematic, sequential phases with numbered steps",
    "architecture diagram": "architecture schematic, flat layered diagram, labeled modules",
    "conceptual illustration": "conceptual schematic, abstract relationship diagram, clean visual metaphor",
    "concept map": "concept map, node-link diagram, hierarchical relationship visualization",
    "data visualization": "data visualization, clean axis labels, statistical plot style",
    "process diagram": "process diagram, stage-transition arrows, annotated phases",
    "schematic": "schematic diagram, technical illustration style, publication-ready",
    "infographic": "academic infographic, flat vector, strong visual hierarchy",
    "network graph": "network graph, node-edge schematic, labeled topology",
    "methodology figure": "methodology figure, flat design, sequential workflow with decision nodes",
}

COMPOSITION_MAP_ACADEMIC = {
    "left-to-right flow": "horizontal left-to-right data flow with directional arrows",
    "top-down": "top-down hierarchical decomposition",
    "matrix layout": "matrix layout with dual-axis, x temporal and y semantic depth",
    "layered": "layered architecture with labeled depths and clear boundaries",
    "radial": "radial arrangement with central node and peripheral elements",
    "grid": "grid layout with aligned cells and consistent spacing",
    "timeline": "horizontal timeline with labeled milestones and connecting arrows",
}

COLOR_MAP_ACADEMIC = {
    "blue-orange": "two-tone academic palette: cool blue for input/process, warm orange for output/result",
    "grayscale": "grayscale academic palette, high contrast suitable for print publication",
    "viridis": "viridis color scale, perceptually uniform and colorblind-safe",
    "cool tones": "cool academic palette in blue-gray tones, clean and restrained",
    "highlight accent": "accent color in gold or amber for key nodes or highlight boxes",
    "sequential": "sequential color gradient from light to dark indicating progression or intensity",
}

AVOID_TERMS = [
    "3D crystal spheres", "glossy buttons", "decorative arcs",
    "outdated bevel effects", "heavy shadows", "glossy fills",
    "artistic distortion", "random text artifacts",
    "photo-realistic texture", "decorative icons",
]

MJ_FLAG_PATTERN = re.compile(r"--[a-zA-Z0-9:_\-.]+(?:\s+[a-zA-Z0-9:.\-]+)?")
WEIGHT_PATTERN = re.compile(r"\(([^()]+):\s*([0-9.]+)\)")
PAREN_BOOST_PATTERN = re.compile(r"\(\(([^()]+)\)\)")


@dataclass
class ConversionResult:
    source_platform: str
    input_prompt: str
    normalized_prompt: str
    converted_prompt: str
    validation: Dict[str, Any]
    comparison: Dict[str, Any]
    extracted: Dict[str, List[str]]


class PaperBananaPromptConverter:
    def detect_platform(self, raw_prompt: str) -> str:
        text = raw_prompt.lower()
        if "--ar" in text or "--stylize" in text or "--v " in text:
            return "midjourney-like"
        if "negative prompt:" in text or "steps:" in text or "sampler:" in text:
            return "stable-diffusion-like"
        if "json" in text and "prompt" in text:
            return "chatgpt-like"
        if "【" in raw_prompt and "】" in raw_prompt:
            return "qwen-like"
        if "输出" in raw_prompt and "提示词" in raw_prompt:
            return "deepseek-like"
        return "generic-llm"

    def parse_multiformat_prompt(self, raw_prompt: str) -> Dict[str, str]:
        parsed = {"prompt": raw_prompt.strip(), "negative": "", "meta": ""}
        json_candidate = raw_prompt.strip()
        if json_candidate.startswith("{") and json_candidate.endswith("}"):
            try:
                data = json.loads(json_candidate)
                if isinstance(data, dict):
                    parsed["prompt"] = str(data.get("prompt", data.get("positive_prompt", parsed["prompt"])))
                    parsed["negative"] = str(data.get("negative_prompt", ""))
                    parsed["meta"] = str(data.get("params", ""))
                    return parsed
            except Exception:
                pass
        inline_neg = re.search(r"negative prompt:\s*(.+)$", raw_prompt, flags=re.IGNORECASE)
        cleaned_input = raw_prompt
        if inline_neg:
            parsed["negative"] = inline_neg.group(1).strip()
            cleaned_input = re.sub(r"negative prompt:\s*.+$", "", raw_prompt, flags=re.IGNORECASE).strip()
        sections = re.split(r"\n+", cleaned_input)
        prompt_lines: List[str] = []
        meta_lines: List[str] = []
        for line in sections:
            low = line.lower().strip()
            if not low:
                continue
            if low.startswith("negative prompt:"):
                parsed["negative"] = line.split(":", 1)[1].strip()
            elif any(low.startswith(k) for k in ["prompt:", "positive prompt:", "提示词：", "提示词:"]):
                prompt_lines.append(line.split(":", 1)[1].strip())
            elif any(low.startswith(k) for k in ["steps:", "cfg", "sampler:", "seed:", "size:", "分辨率"]):
                meta_lines.append(line.strip())
            else:
                prompt_lines.append(line.strip())
        if prompt_lines:
            parsed["prompt"] = ", ".join(prompt_lines)
        if meta_lines:
            parsed["meta"] = " | ".join(meta_lines)
        return parsed

    def normalize_prompt(self, prompt: str) -> str:
        text = prompt
        text = MJ_FLAG_PATTERN.sub("", text)
        text = WEIGHT_PATTERN.sub(r"\1", text)
        text = PAREN_BOOST_PATTERN.sub(r"\1", text)
        text = re.sub(r"\s{2,}", " ", text)
        text = re.sub(r"\s*,\s*", ", ", text).strip(" ,")
        return text

    def extract_keywords(self, prompt: str) -> Dict[str, List[str]]:
        low = prompt.lower()
        styles = [v for k, v in STYLE_MAP.items() if k in low]
        styles_academic = [v for k, v in STYLE_MAP_ACADEMIC.items() if k in low]
        quality = [v for k, v in QUALITY_MAP.items() if k in low]
        composition = [v for k, v in COMPOSITION_MAP.items() if k in low]
        composition_academic = [v for k, v in COMPOSITION_MAP_ACADEMIC.items() if k in low]
        colors = [v for k, v in COLOR_MAP.items() if k in low]
        colors_academic = [v for k, v in COLOR_MAP_ACADEMIC.items() if k in low]
        entities = []
        chunks = [c.strip() for c in re.split(r"[,.;\n]", prompt) if c.strip()]
        for c in chunks:
            if len(c.split()) >= 3 and len(entities) < 6:
                entities.append(c)
        return {
            "style": (styles + styles_academic)[:3],
            "quality": quality[:3],
            "composition": (composition + composition_academic)[:3],
            "color": (colors + colors_academic)[:3],
            "entities": entities[:4],
        }

    def compose_paperbanana_prompt(self, extracted: Dict[str, List[str]], negative: str = "") -> str:
        subject = extracted["entities"][0] if extracted["entities"] else "a clear and meaningful main subject"
        scene = extracted["entities"][1] if len(extracted["entities"]) > 1 else "a context-rich environment with coherent details"
        style = ", ".join(extracted["style"]) if extracted["style"] else "clean scientific visual style"
        comp = ", ".join(extracted["composition"]) if extracted["composition"] else "balanced composition with clear focal hierarchy"
        color = ", ".join(extracted["color"]) if extracted["color"] else "harmonized color palette with controlled contrast"
        quality = ", ".join(extracted["quality"]) if extracted["quality"] else "high detail, sharp structure, publication-ready quality"
        parts = [
            f"Main subject: {subject}",
            f"Scene and context: {scene}",
            f"Visual style: {style}",
            f"Composition: {comp}",
            f"Color and lighting: {color}",
            f"Quality target: {quality}",
        ]
        if negative.strip():
            cleaned_negative = self.normalize_prompt(negative)
            if cleaned_negative:
                parts.append(f"Avoid: {cleaned_negative}")
        parts.append(f"Output requirement: clear structure, no watermark, no random text artifacts, clean background suitable for publication")
        avoid_str = ", ".join(AVOID_TERMS)
        parts.append(f"Avoid decorative elements: {avoid_str}")
        return "; ".join(parts)

    def validate_prompt(self, converted_prompt: str) -> Dict[str, Any]:
        checks = {
            "length_ok": 80 <= len(converted_prompt) <= 900,
            "has_subject": "Main subject:" in converted_prompt,
            "has_style": "Visual style:" in converted_prompt,
            "has_composition": "Composition:" in converted_prompt,
            "has_color": "Color and lighting:" in converted_prompt,
            "has_quality": "Quality target:" in converted_prompt,
            "mj_flags_removed": "--ar" not in converted_prompt and "--stylize" not in converted_prompt,
            "weight_syntax_removed": "((" not in converted_prompt and re.search(r"\([^)]+:[0-9.]+\)", converted_prompt) is None,
        }
        score = round(sum(1 for v in checks.values() if v) / len(checks) * 100, 2)
        return {"is_valid": all(checks.values()), "score": score, "checks": checks}

    def score_prompt_for_paperbanana(self, prompt: str) -> Dict[str, Any]:
        dimensions = ["1024x1024", "1024x768", "768x1024", "1920x1080"]
        text = prompt.lower()
        rubric = {
            "specific_subject": len(prompt.split()) >= 12,
            "includes_style": any(k in text for k in STYLE_MAP.keys()),
            "includes_composition": any(k in text for k in COMPOSITION_MAP.keys()),
            "includes_color_light": any(k in text for k in COLOR_MAP.keys()) or "lighting" in text or "color" in text,
            "contains_hard_flags": bool(MJ_FLAG_PATTERN.search(prompt)),
            "has_readability_goal": "clear" in text or "readability" in text or "publication" in text,
            "suggested_dimension_mentioned": any(d in prompt for d in dimensions),
        }
        positive = sum(1 for k, v in rubric.items() if v and k != "contains_hard_flags")
        if rubric["contains_hard_flags"]:
            positive -= 1
        score = max(0, min(100, int(positive / 6 * 100)))
        return {"score": score, "rubric": rubric}

    def compare_before_after(self, before: str, after: str) -> Dict[str, Any]:
        before_score = self.score_prompt_for_paperbanana(before)
        after_score = self.score_prompt_for_paperbanana(after)
        return {
            "before_score": before_score["score"],
            "after_score": after_score["score"],
            "improvement": after_score["score"] - before_score["score"],
            "before_rubric": before_score["rubric"],
            "after_rubric": after_score["rubric"],
        }

    def convert(self, raw_prompt: str) -> ConversionResult:
        platform = self.detect_platform(raw_prompt)
        parsed = self.parse_multiformat_prompt(raw_prompt)
        normalized = self.normalize_prompt(parsed["prompt"])
        extracted = self.extract_keywords(normalized)
        converted = self.compose_paperbanana_prompt(extracted, parsed.get("negative", ""))
        validation = self.validate_prompt(converted)
        comparison = self.compare_before_after(raw_prompt, converted)
        return ConversionResult(
            source_platform=platform,
            input_prompt=raw_prompt,
            normalized_prompt=normalized,
            converted_prompt=converted,
            validation=validation,
            comparison=comparison,
            extracted=extracted,
        )


def run_single_conversion(raw_prompt: str) -> Dict[str, Any]:
    converter = PaperBananaPromptConverter()
    result = converter.convert(raw_prompt)
    return {
        "source_platform": result.source_platform,
        "input_prompt": result.input_prompt,
        "normalized_prompt": result.normalized_prompt,
        "converted_prompt": result.converted_prompt,
        "validation": result.validation,
        "comparison": result.comparison,
        "extracted": result.extracted,
    }


if __name__ == "__main__":
    sample = "((Best quality)), cinematic landscape, mountain lake, warm tones, low angle --ar 16:9 --stylize 500"
    output = run_single_conversion(sample)
    print(json.dumps(output, ensure_ascii=False, indent=2))
