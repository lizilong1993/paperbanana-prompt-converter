# paperbanana-prompt-converter

将 ChatGPT、DeepSeek、通义千问、Midjourney/Stable Diffusion 风格提示词，转换为更适配 PaperBanana 的结构化提示词。

## 功能概览
- 自动识别多平台提示词格式
- 清理不兼容语法（如 `--ar`、`--stylize`、权重括号）
- 提取主体、场景、风格、构图、色彩、质量要素并重组
- 输出可直接粘贴到 PaperBanana 的优化提示词
- 提供有效性校验与转换前后评分对比

## 目录结构
- `SKILL.md`：Skill 定义与调用说明
- `paperbanana_converter.py`：核心解析与转换逻辑
- `test_cases.json`：测试用例（人物/风景/抽象/科研示意等）
- `run_tests.py`：测试脚本

## 安装到 Trae
将本目录放入你的项目路径：

```text
<your-project>/.trae/skills/paperbanana-prompt-converter/
```

确保存在：

```text
<your-project>/.trae/skills/paperbanana-prompt-converter/SKILL.md
```

## 使用方式
在该目录执行：

```bash
python paperbanana_converter.py
python run_tests.py
```

在 Trae 中可直接调用 skill 名称：

```text
paperbanana-prompt-converter
```

## 输入示例

```markdown
cinematic landscape of alpine valley at sunrise, dramatic clouds, ultra detailed, low angle, warm tones --ar 16:9 --stylize 750 --v 6
```

## 输出示例

```markdown
Main subject: cinematic landscape of alpine valley at sunrise; Scene and context: dramatic clouds; Visual style: cinematic composition with strong storytelling; Composition: low-angle perspective for visual impact; Color and lighting: warm color temperature with soft highlights; Quality target: fine-grained texture and structure; Output requirement: clear structure, no watermark, no random text artifacts
```

## 在 GitHub 分享
1. 在 GitHub 新建仓库（如 `paperbanana-prompt-converter-skill`）
2. 在本目录执行：

```bash
git init
git add .
git commit -m "feat: add paperbanana prompt converter skill"
git branch -M main
git remote add origin https://github.com/<your-name>/paperbanana-prompt-converter-skill.git
git push -u origin main
```

3. 让他人克隆后复制到其项目的 `.trae/skills/` 下即可使用
