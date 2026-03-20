---
name: "paperbanana-prompt-converter"
description: "将 ChatGPT/DeepSeek/通义千问等绘图提示词转换为 PaperBanana 最优格式。在用户要跨平台迁移提示词、提升 PaperBanana 出图稳定性时调用。"
---

# PaperBanana Prompt Converter

## 适用场景
- 用户提供来自 ChatGPT、DeepSeek、通义千问或 Midjourney/Stable Diffusion 风格提示词
- 用户希望迁移到 PaperBanana 并提升生成质量与一致性
- 用户需要转换前后对比与可验证的效果评分

## 平台分析结论（基于 https://paperbanana.me/ 可访问页面与前端配置）
- Text to Image 入口显示主要模型为 Wan 2.5，强调高保真与创作灵活性
- 可见尺寸选项：`1024x1024`、`1024x768`、`768x1024`、`1920x1080`
- FAQ 明确建议提示词应“具体且描述性强”，尤其包含风格、色彩、构图信息
- 可见示例偏向自然语言和结构化短句，不依赖复杂参数串
- 平台展示支持多种风格：写实、卡通、油画、数字艺术等

## 转换策略
1. 识别来源格式
   - JSON 格式（`prompt`、`negative_prompt`）
   - Prompt/Negative Prompt 分段文本
   - Midjourney 风格参数（`--ar`、`--stylize`、`--v`）
   - Stable Diffusion 权重语法（`((...))`、`(token:1.2)`）
2. 语法清洗与归一化
   - 去除不兼容硬参数
   - 降级权重语法为普通描述
   - 合并碎片词段为语义完整短句
3. 关键词提取重组
   - 主体、场景、风格、构图、色彩、质量目标六段式重组
4. 有效性校验
   - 校验必要字段是否齐全
   - 校验遗留不兼容语法是否清除
   - 计算转换质量分数
5. 效果对比
   - 转换前后按 PaperBanana 适配 Rubric 打分
   - 输出提升分值和差异明细

## 标准化映射表

| 类别 | 通用词 | PaperBanana 优化词 |
|---|---|---|
| 风格 | photorealistic / realistic | photorealistic, publication-ready rendering |
| 风格 | cinematic | cinematic composition with strong storytelling |
| 风格 | digital art | clean digital illustration, publication-ready quality |
| 风格 | scientific diagram | scientific diagram style, clear labels, high readability |
| 质量 | best quality / masterpiece | ultra clear details / high aesthetic quality |
| 构图 | close-up / low angle / top view | close-up framing / low-angle perspective / top-down composition |
| 色彩 | vibrant / muted / monochrome | controlled vibrant palette / muted soft-contrast / tonal monochrome |

## 交付文件
- `paperbanana_converter.py`：解析、转换、验证、对比主实现
- `test_cases.json`：覆盖人物、风景、抽象、科研示意、SD 格式样例
- `run_tests.py`：批量运行转换效果测试

## 使用方式
在该目录执行：

```bash
python paperbanana_converter.py
python run_tests.py
```

## 输入输出示例

输入（DeepSeek/MJ风格）：

```text
cinematic landscape of alpine valley at sunrise, dramatic clouds, ultra detailed, low angle, warm tones --ar 16:9 --stylize 750 --v 6
```

输出（PaperBanana优化）：

```text
Main subject: cinematic landscape of alpine valley at sunrise; Scene and context: dramatic clouds; Visual style: cinematic composition with strong storytelling; Composition: low-angle perspective for visual impact; Color and lighting: warm color temperature with soft highlights; Quality target: fine-grained texture and structure; Output requirement: clear structure, no watermark, no random text artifacts
```

## 执行规范
- 优先保留语义，不机械直译
- 默认补全“可读性、结构清晰、无水印与文本伪影”质量约束
- 若输入缺少风格/构图/色彩信息，自动补足最小可用描述
- 输出应可直接粘贴至 PaperBanana 文本输入框使用
