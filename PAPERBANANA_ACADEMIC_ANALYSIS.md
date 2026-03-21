# PaperBanana 学术提示词深度分析报告

> 数据来源：`https://paperbanana.me/#features` 页面所有可解析提示词示例
> 生成时间：2026-03-21

---

## 一、页面提示词逐条分析

### 1.1 Text-to-Image 官方示例（学术类）

| ID | 提示词原文 | 学术风格 | 判断依据 | 学科领域 |
|----|-----------|---------|---------|---------|
| T1 | `Scientific diagram showing cell division process` | **科学流程图（Scientific Diagram）** | 明确使用 "Scientific diagram" 触发词，"showing process" 表明阶段递进语义，隐含分步骤可视化需求 | 细胞生物学 / 生命科学 |
| T2 | `Architecture diagram of a neural network with labeled layers` | **架构图（Architecture Diagram）** | "Architecture diagram" 是 CV/AI 领域标准图示类型，"with labeled layers" 强调层级标注，符合神经网络技术文档惯例 | 计算机视觉 / 人工智能 |
| T3 | `Flowchart of experimental methodology` | **方法论流程图（Methodology Flowchart）** | "Flowchart" 直接定位，"experimental methodology" 表明实验步骤顺序与条件分支逻辑 | 通用科研 / 实验科学 |
| T4 | `Conceptual illustration of quantum entanglement` | **概念示意图（Conceptual Illustration / Schematic）** | "Conceptual illustration" 表明抽象概念可视化，"quantum entanglement" 超出日常经验需概念化表达 | 量子物理 / 基础科学 |

### 1.2 营销页面通用示例（非学术类）

以下为 PaperBanana 官网用于展示通用创作能力的示例，**不直接适用于学术场景**，但可供分析其风格分布：

| ID | 提示词原文 | 风格类型 | 学科领域 | 说明 |
|----|-----------|---------|---------|------|
| P1 | `A drone captures waves crashing against the rugged cliffs...` | 自然景观摄影叙事 | 地理学/海洋学 | 含具体地点（Garrapata Beach），强调光影与构图，接近风景摄影 |
| P2 | `Several gigantic mammoths are slowly walking toward us...` | 自然纪录片风格 | 古生物学/生态学 | 低角镜头叙事，"herd of furry giants" 具象化史前生物 |
| P3 | `Animation scene close-up: a fluffy little monster...` | 3D 动画特写 | 通用创意 | "3D realistic" + "warm tones"，聚焦纹理与光影 |
| P4 | `New York City is submerged in water like Atlantis` | 概念场景渲染 | 城市研究/气候变化 | 虚构场景，用于展示概念想象能力 |
| P5 | `[视频提示词] hand in black glove holding a knife...` | 精密工艺视频 | 通用 | ASMR 质感，短焦固定机位 |
| P6 | `[Midjourney风格] --ar 73:110 --stylize 750` | 人像艺术摄影 | 时尚/摄影 | 引用相机型号/OSHAKE KEI 风格标签 |
| P7 | `[Midjourney风格] Cherry blossoms and the moon in the style of Ukiyo-e` | 浮世绘风格合成 | 艺术史/日本文化 | 明确引用 Ukiyo-e 艺术风格 |
| P8 | `((Best quality)) celestial sailing ship... In the style of J. M. W. Turner` | 学院派数字绘画 | 天文/艺术史 | 引用具体画家风格（Turner），天文场景 |
| P9 | `Realistic portrait of Yor Forger... VOGUE magazine cover` | 时尚杂志人像 | 时尚/媒体 | 商业时尚摄影构图 |
| P10 | `Miniature Chilean dish... tiny animated figures... 360 orbit` | 3D 食品动画 | 食品科学/文化人类学 | 精密道具感，工程视角 |
| P11 | `Double exposure, Midjourney style... Arthur Morgan silhouette...` | 双曝光概念合成 | 数字艺术 | 双重曝光技术引用，叙事性插画 |

### 1.3 Text-to-Image 示例（短句类）

| ID | 提示词 | 风格 | 领域 | 说明 |
|----|-------|------|------|------|
| S1 | `Beautiful portrait with soft natural lighting` | 基础人像 | 通用 | 极简风格触发词，"soft natural lighting" 限定光影 |
| S2 | `Cinematic landscape with dramatic lighting` | 电影感风景 | 影视/地理 | "cinematic" + "dramatic lighting" 组合 |
| S3 | `Abstract digital art with vibrant colors` | 抽象数字艺术 | 通用 | "abstract" + "vibrant colors" 无领域绑定 |
| S4 | `Professional product photography` | 专业产品摄影 | 商业/电商 | 极简短句，无细节约束 |

### 1.4 ImageEdit 示例

| ID | 提示词 | 功能类型 | 适用场景 |
|----|-------|---------|---------|
| E1 | `Convert this photo into academic illustration style` | 风格转换 | 照片→学术图 |
| E2 | `Add labels and annotations to this diagram` | 标注增强 | 增强可读性 |
| E3 | `Enhance colors and add scientific markers` | 色彩优化 | 数据可视化增色 |
| E4 | `Transform into publication-ready figure` | 出版级处理 | 终态输出 |

### 1.5 IllustrationEditor 示例

| ID | 提示词 | 编辑目标 |
|----|-------|---------|
| IE1 | `Adjust the color scheme to match journal requirements` | 配色适配（期刊标准） |
| IE2 | `Add scale bar and axis labels` | 技术规范（比例尺/坐标轴） |
| IE3 | `Simplify the background for better clarity` | 简化背景 |
| IE4 | `Enhance contrast for print publication` | 印刷对比度优化 |

---

## 二、提示词—学术风格—图示类型 三元组对照表

### 2.1 核心规律提炼

#### 高频关键词库

**学术风格触发词（第一优先级）：**
```
Scientific diagram / Architecture diagram / Flowchart /
Conceptual illustration / Schematic / Process map /
Methodology figure / Statistical plot / Data visualization /
Concept map / Infographic / Network graph
```

**构图与结构关键词：**
```
labeled layers / with annotations / with arrows / stage transitions /
hierarchical / with legend / with scale bar / with axis labels /
numbered steps / color-coded / annotated
```

**质量与输出关键词：**
```
publication-ready / journal quality / clear labels /
high readability / clean background / no watermark /
balanced composition / concise / rigorous
```

**避忌词（PaperBanana 学术场景不应出现）：**
```
3D crystal spheres / glossy buttons / decorative arcs /
heavy shadows / bevel effects / artistic distortion /
random text artifacts / low contrast (for print)
```

#### 句式结构规律

**结构 A（流程/阶段类）：**
```
[类型词] showing [核心过程/实体] + [附加修饰]
示例：Scientific diagram showing cell division process
```

**结构 B（架构/层级类）：**
```
[类型词] of [系统名] + [with 标注要求]
示例：Architecture diagram of a neural network with labeled layers
```

**结构 C（方法论类）：**
```
[类型词] of [研究内容]
示例：Flowchart of experimental methodology
```

**结构 D（概念/抽象类）：**
```
[类型词] of [抽象概念]
示例：Conceptual illustration of quantum entanglement
```

#### 参数化模板

| 模板类型 | 句式 | 示例 |
|---------|------|------|
| 流程图 | `[Style] showing [process] with [annotations]` | `Scientific diagram showing [ENTITY] process with labeled stages` |
| 架构图 | `[Style] of [system] with [labels]` | `Architecture diagram of [ARCHITECTURE] with labeled layers` |
| 概念图 | `[Style] of [concept]` | `Conceptual illustration of [CONCEPT]` |
| 方法流程图 | `[Style] of [methodology]` | `Flowchart of experimental methodology` |
| 数据可视化 | `[Type] with [color scheme] + [axis labels]` | `Statistical plot with [COLOR_THEME] and axis labels` |
| 概念图谱 | `[Style] showing relationship between X and Y` | `Concept map showing relationship between [A] and [B]` |

---

## 三、高质量提示词优化准则

### 3.1 风格一致性检查清单

#### 学科动词规范
| 场景 | 动词 | 禁用词 |
|------|------|-------|
| 流程图 | "showing process", "illustrating stages", "depicting transitions" | "drawing", "painting" |
| 架构图 | "illustrating structure", "showing architecture", "depicting layers" | "drawing", "sketching" |
| 概念图 | "illustrating concept", "visualizing relationship", "showing mechanism" | "drawing", "painting" |
| 方法论图 | "showing methodology", "illustrating workflow", "depicting pipeline" | "drawing" |
| 统计图 | "showing distribution", "illustrating comparison", "depicting trend" | "drawing" |

#### 时态规范
- 学术图表**一律使用现在时**（展示客观存在的关系/过程）
- 禁用过去时、虚拟语气等主观叙事时态

#### 缩写规范
- 首次出现写全称 + 括号内附缩写（如：Convolutional Neural Network (CNN)）
- 标准缩写直接使用：OLAP, ARD, CNN, RNN, LSTM, GIS, GPS
- 中文期刊：部分国内期刊要求全称优先

#### 引用格式（图表脚注）
- 图表应自含说明，不依赖正文上下文
- 颜色映射需在图例中标注实际含义

### 3.2 图示需求描述模板

#### 模板 A：流程/阶段型
```
[Style] showing [PROCESS_NAME] with [N] stages:
Stage 1: [SUB_PROCESS_A]
Stage 2: [SUB_PROCESS_B]
...
Stage N: [SUB_PROCESS_N]
Requirements: [numbered annotations / arrows between stages / color-coded by PHASE / legend at bottom]
Output: publication-ready, no watermark, clear labels
```

#### 模板 B：架构/层级型
```
[Style] of [SYSTEM_NAME] architecture with [LAYER_COUNT] layers:
- Input layer: [DESCRIPTION]
- Hidden layer(s): [DESCRIPTION]
- Output layer: [DESCRIPTION]
Connections: [forward / bidirectional / skip connections]
Requirements: labeled layers, connection arrows, activation annotations
Style: [flat / schematic / publication diagram]
```

#### 模板 C：概念/关系型
```
[Style] illustrating the relationship between [CONCEPT_A] and [CONCEPT_B]:
Key elements:
- [ELEMENT_1]: [DESCRIPTION]
- [ELEMENT_2]: [DESCRIPTION]
Relationship: [TYPE: causal / correlational / hierarchical / sequential]
Style: [schematic / conceptual / abstract]
Color coding: [MEANING OF COLORS]
```

#### 模板 D：数据/比较型
```
[CHART_TYPE] comparing [VARIABLE_A] vs [VARIABLE_B] across [CONDITION]:
Axes: X=[VARIABLE] with unit, Y=[VARIABLE] with unit
Data series: [SERIES_1], [SERIES_2], ...
Legend: [位置 and meaning]
Statistical annotation: [p-value / significance level if applicable]
Style: clean axis lines, gridlines optional, no chart junk
```

### 3.3 可扩展参数占位符设计

```python
PLACEHOLDER_SCHEME = {
    # === 期刊/出版参数 ===
    "{{JOURNAL_NAME}}": "Nature / Science / IEEE Transactions ...",
    "{{FIGURE_NUMBER}}": "Fig. 1 / Figure 2 ...",
    "{{RESOLUTION}}": "300 dpi (print) / 150 dpi (web)",

    # === 颜色主题参数 ===
    "{{COLOR_THEME}}": "bluescale / viridis / grayscale / journal-standard",
    "{{PRIMARY_COLOR}}": "#2171B5 (blue) / #D94801 (orange) ...",
    "{{ACCENT_COLOR}}": "#F0F0F0 (light gray) ...",

    # === 学科领域参数 ===
    "{{DOMAIN}}": "CV / NLP / Remote Sensing / Medicine / Biology ...",

    # === 系统/模型参数 ===
    "{{MODEL_NAME}}": "ResNet-50 / BERT / Swin Transformer ...",
    "{{ARCHITECTURE}}": "encoder-decoder / transformer / CNN ...",
    "{{LAYER_CONFIG}}": "N layers, M heads, K dimensions",

    # === 数据/流程参数 ===
    "{{DATASET_NAME}}": "ImageNet / COCO /自定义数据集名",
    "{{DATASET_PATH}}": "/path/to/dataset",
    "{{PROCESS_NAME}}": "preprocessing / training / inference ...",
    "{{N_STAGES}}": "3 / 5 / N stages",
    "{{STAGE_I_NAME}}": "stage name",
    "{{STAGE_I_OUTPUT}}": "output description",

    # === 标签/标注参数 ===
    "{{AXIS_X_LABEL}}": "X轴变量名 (单位)",
    "{{AXIS_Y_LABEL}}": "Y轴变量名 (单位)",
    "{{LEGEND_POSITION}}": "bottom-right / top-left / outside",
    "{{ANNOTATION_TEXT}}": "显著性标注 e.g. p<0.05",

    # === 避忌参数 ===
    "{{AVOID}}": "no 3D spheres, no decorative arcs, no heavy shadows",
}
```

**批量替换使用示例：**
```
输入模板：
"[Style] showing {{PROCESS_NAME}} with {{N_STAGES}} stages..."
替换后：
"[Style] showing Model Training Pipeline with 5 stages..."
```

---

## 四、学术风格版本优化示例（3个版本）

### 版本一：神经网络架构图（计算机视觉领域）

**原始输入（通用描述）：**
```
Architecture diagram of a neural network with labeled layers
```

**优化后 PaperBanana 提示词（V1.0）：**

```
Main subject: Encoder-decoder architecture for image semantic segmentation with skip connections

Scene and context: Clean architectural schematic showing data flow from input image through encoder stages (Conv-BN-ReLU pooling) to bottleneck, then through decoder stages (upsampling-concatenation) to pixel-level output mask

Visual style: flat schematic diagram, publication-ready quality, high readability, academic illustration style with consistent line weights and clear component boundaries

Composition:
- Horizontal left-to-right data flow: Input Image → Encoder (4 stages with channel info: 64→128→256→512) → Bottleneck → Decoder (4 stages: 512→256→128→64) → Output Mask
- Above architecture: skip connections shown as dashed arrows from encoder stages to corresponding decoder stages
- Below each module: brief label (e.g. "Conv 3×3, BN, ReLU" / "Max Pool 2×2")

Color and lighting: Two-tone academic palette (encoder in cool blue tones, decoder in warm orange tones), output mask in green accent, white background, no gradient fills, no shadows, uniform line color for connections

Quality target: All layers labeled with module name and hyperparameter config, arrows indicate data direction, legend at bottom-right explains line styles, balanced whitespace, no watermark, suitable for IEEE/ACM publication

Avoid: 3D perspective, decorative arrows, gradient fills, heavy borders, photographic textures, random text artifacts

Text language: Use standard English technical terms with Chinese labels in parentheses where first introduced. Keep all text concise and typeset at consistent font size.
```

**预期图示描述：**
> 左右流向的横向架构图。左侧输入框（图像）向右依次通过 4 个蓝色编码器块（每块标注 Conv-BN-ReLU + 通道数），经灰色瓶颈层后进入 4 个橙色解码器块，虚线从各编码器跨连接到同级解码器，最右侧输出分割掩码图（绿色边框）。底部有线条样式图例，右下角有模块名称缩略对照表。无阴影、无立体感、线条均匀、留白充足。

---

### 版本二：实验方法论流程图（通用科研）

**原始输入（通用描述）：**
```
Flowchart of experimental methodology
```

**优化后 PaperBanana 提示词（V2.0）：**

```
Main subject: Experimental methodology flowchart for [RESEARCH_TOPIC] with [N] sequential phases

Scene and context: Clean left-to-right horizontal flowchart showing complete research pipeline from problem definition to conclusion, with decision nodes and alternative paths clearly distinguished

Visual style: methodology flowchart, schematic diagram, publication-ready, high readability, flat design with uniform box heights and consistent arrow styles

Composition:
- Phase 1 (leftmost): Problem Definition & Literature Review → rectangular box, light gray fill
- Phase 2: Data Collection → rectangular box, light blue fill
- Phase 3: [Custom Phase Name] → rectangular box, light yellow fill
- ...
- Decision node(s): diamond shape(s) with YES/NO branches
- Termination node(s): rounded rectangle (Conclusion / Reject)
- All boxes connected by single-direction arrows (no bidirectional arrows)
- Each box contains: phase name (bold) + 1-line brief activity description below

Color and lighting: Phase-dependent color coding (max 5 distinct light pastels), white background, black text and arrows, no gradient, no shadow, no decorative elements

Quality target: Sequential numbering (Phase 1, Phase 2...), branch labels (YES/NO), legend explaining color meaning at bottom, figure number and caption below, suitable for NSFC/研究申报材料 or journal submission

Avoid: 3D boxes, bevel effects, circular arrows, decorative icons inside boxes, heavy outlines, photographic elements, artistic embellishments

Text language: Chinese primary text with English technical terms in parentheses on first use. Keep box text to ≤15 Chinese characters per line, maximum 2 lines per box. Arrow labels ≤5 Chinese characters.
```

**预期图示描述：**
> 横向流程图，左起 Phase 1 方框（灰底：问题定义+文献综述），右箭头指向 Phase 2 方框（浅蓝底：数据采集），再指向 Phase 3、4... 直至末端圆角方框（结论）。决策节点（菱形）位于某阶段后，分出 YES（向下）和 NO（向左回环）两条路径。底部有图例说明颜色含义，图的下方有图号和简短英文图说明。无阴影、无立体框、无装饰图标。

---

### 版本三：时空数据演进概念图（遥感/地信领域，适配 NSFC 申报）

**原始输入（用户提供的长提示词）：**
```
Create a high quality academic infographic for a National Natural Science Foundation of China proposal. The figure should have a white background, clean flat vector style, modern and rational academic aesthetics, and clear labeling suitable for a research proposal and journal paper. The theme is the technological evolution of spatiotemporal data cubes from static physical organization to dynamic semantic organization...
```

**优化后 PaperBanana 提示词（V3.0）：**

```
Main subject: 时空数据立方体技术演进概念图——从静态物理组织到动态语义组织（适配国家自然科学基金申请书与期刊论文）

Scene and context: 白色背景，横向时间轴（1990s→2010s→2020-2025→2026+）× 纵向语义深度轴（像元级→场景级→目标级→事件级）构成的二维矩阵框架；右侧高亮学术风格框标注"本项目定位"

Visual style: clean flat vector infographic, scientific diagram style, publication-ready, modern rational academic aesthetics, strong visual hierarchy, high readability

Composition:
- 横轴时间轴（从左至右，向上箭头表示时间演进）：
  ① 1990s：多维数组与 OLAP（标注英文全称：Online Analytical Processing）
  ② 2010s：Open Data Cube 与 ARD（Analysis Ready Data）
  ③ 2020–2025：Earth Video Cube 与 VideoARD
  ④ 2026+：复杂观测条件下的遥感视频语义立方体
- 纵轴语义深度轴（从下至上，带箭头）：
  像元级（Pixel level）→ 场景级（Scene level）→ 目标级（Object level）→ 事件级（Event level）
- 各阶段与各语义层级之间用细实线箭头表示"能力递进"和"组织范式升级"
- 右侧（本项目定位框）：浅黄/金色边框高亮学术风格框，内含关键词：
  · 复杂观测条件
  · 语义分析就绪（Analysis-Ready）
  · 场景-目标-事件（Scene-Object-Event）
  · 实体流组织（Entity Stream Organization）

Color and lighting: 低饱和学术配色方案——主色调为蓝灰（#4A90A4）与青灰（#5B8C8C）；时间轴节点用深蓝圆点；纵轴标签用深灰；"本项目定位"框用浅金边框（#D4A843）+ 浅黄填充；远离高饱和色、渐变、阴影；白底黑灰文字

Quality target: 所有坐标轴和节点均有短标注（≤10个汉字或≤20个英文字母）；中英混排时英文缩写首次出现附中文注释；图例放底部或右侧；图下方：Figure X. [英文简短标题]（中文图题加粗）；线条均匀、留白均衡；无水印、无文字伪影；适配 1920×1080 或 1024×768 输出

Avoid: 3D水晶球、立体球、光泽按钮、装饰性弧线、过时浮雕效果、厚重阴影、炫光、照片质感背景、无意义图标装饰

Text policy: 标题、轴标签、节点标注、注释、说明框、图注全部使用简体中文；仅保留标准学术缩写/既有技术名词英文：OLAP, ARD, Open Data Cube, VideoARD, Earth Video Cube；其余文本均为简洁中文≤10字/条

Output requirement: Publication-ready, no watermark, no random text artifacts, 清晰可辨且字重统一
```

**预期图示描述：**
> 16:9 比例，白底，双轴学术信息图。横轴标注四个发展阶段（各附英文技术缩写），纵轴标注四级语义深度（像素→场景→目标→事件），两者交汇处标注该阶段能力特征。右侧有金色边框高亮框"本项目定位"，内列四个关键词。全图线条均匀、色调克制、无装饰元素。适合直接插入 NSFC 申请书 PDF 或期刊论文 LaTeX。

---

## 五、paperbanana_converter.py 映射表扩充建议

基于以上分析，建议在 `STYLE_MAP` 中新增学术专用风格：

```python
STYLE_MAP_ACADEMIC = {
    "scientific diagram": "scientific diagram style, clear labels, high readability",
    "flowchart": "methodology flowchart, flat schematic, sequential phases with numbered steps",
    "architecture diagram": "architecture schematic, flat layered diagram, labeled modules",
    "conceptual illustration": "conceptual schematic, abstract relationship diagram, clean visual metaphor",
    "concept map": "concept map, node-link diagram, hierarchical relationship visualization",
    "data visualization": "data visualization, clean axis labels, statistical plot style",
    "process diagram": "process diagram, stage-transition arrows, annotated phases",
    "schematic": "schematic diagram, technical illustration style, publication-ready",
    "infographic": "academic infographic, flat vector, strong visual hierarchy",
    "network graph": "network graph, node-edge schematic, labeled topology",
}

COMPOSITION_MAP_ACADEMIC = {
    "left-to-right flow": "horizontal left-to-right data flow with directional arrows",
    "top-down": "top-down hierarchical decomposition",
    "matrix layout": "matrix layout with dual-axis (x: temporal, y: semantic depth)",
    "layered": "layered architecture with labeled depths",
    "radial": "radial arrangement with central node and peripheral elements",
}

COLOR_MAP_ACADEMIC = {
    "blue-orange": "two-tone academic palette: blue (input/process) and orange (output/result)",
    "grayscale": "grayscale academic palette, high contrast for print",
    "viridis": "viridis color scale, perceptually uniform, colorblind-safe",
    "cool tones": "cool academic palette (blue-gray tones), clean and restrained",
    "highlight accent": "accent color (gold/amber) for key nodes or highlight boxes",
}
```

---

## 六、核心发现摘要

1. **PaperBanana 学术提示词句式高度模板化**，核心结构为 `[Style] + [Content] + [with Annotations]`，三元纽分词组合即可覆盖 80% 场景。

2. **短句式直接触发风格分类**：官网示例中 `Scientific diagram`、`Architecture diagram`、`Flowchart`、`Conceptual illustration` 四条即可完整覆盖主流学术图示需求。

3. **颜色与光影在学术场景中服务于信息编码**，而非装饰性；需在提示词中明确"色盲安全"、"高对比度"、"白底"等约束。

4. **中文 NSFC 申报场景需要额外约束**：需在提示词末尾附加 `Text policy: 中文主文本，英文缩写首次附注，极短标签，避免长句` 一类指令，以避免 AI 生成不必要的长中文段落。

5. **避忌列表应作为学术提示词的固定尾部约束**，因为 PaperBanana 底层模型会优先保留描述性内容，忽略避忌词会导致生成图含非学术装饰元素。
