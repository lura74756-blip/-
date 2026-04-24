# 🐱 猫语识别软件 - Cat Language Recognition System

一个智能的猫语识别系统，能够识别和解释猫的各种叫声及其情感状态。

An intelligent cat language recognition system that can identify and interpret various cat sounds and emotional states.

## ✨ 功能特性 - Features

### 🎯 核心功能
- **6 种猫叫声识别**: Meow、Purr、Hiss、Growl、Chirp、Yowl
- **情感推断**: 自动识别猫咪的情感状态 (Happy、Angry、Distressed、Playful、Alert)
- **交流解释**: 提供猫叫声的含义解释
- **交互建议**: 根据情感状态提供人类应该如何回应的建议
- **高级音频分析**: 包含 MFCC、频谱质心、零交叉率、基频检测等特征提取

### 🔊 支持的猫叫声

| 叫声 | 含义 | 情感状态 |
|------|------|----------|
| **Meow** | 想引起你的注意 | Distressed / Playful |
| **Purr** | 很满足和放松 | Happy |
| **Hiss** | 感到威胁或生气 | Angry |
| **Growl** | 感到愤怒或不适 | Angry / Alert |
| **Chirp** | 很兴奋或想玩耍 | Playful / Happy |
| **Yowl** | 发情期或感到沮丧 | Distressed |

## 📋 安装 - Installation

### 系统要求 - System Requirements
- Python 3.7+
- pip 或 conda

### 安装步骤

```bash
# 1. 克隆仓库
git clone https://github.com/lura74756-blip/lura74756-blip.git
cd lura74756-blip

# 2. 安装依赖
pip install -r requirements.txt
```

## 🚀 快速开始 - Quick Start

### 基础使用

```python
from cat_sound_recognizer import CatSoundRecognizer
import numpy as np

# 初始化识别器
recognizer = CatSoundRecognizer()

# 准备音频数据 (示例：生成的音频数据)
audio_data = np.random.randn(16000)  # 1 秒的音频，采样率 16000 Hz

# 识别猫叫声
result = recognizer.recognize_sound(audio_data, sample_rate=16000)

# 获取结果
print(f"识别的声音: {result['sound']}")
print(f"信置度: {result['confidence']:.2%}")
print(f"情感状态: {result['emotion']}")

# 获取解释和建议
interpretation = recognizer.interpret_communication(result['sound'])
suggestion = recognizer.get_response_suggestion(result['sound'], result['emotion'])

print(f"解释: {interpretation}")
print(f"建议: {suggestion}")
```

### 运行示例

```bash
python example_usage.py
```

这将运行完整的演示，包括：
1. 对所有 6 种猫叫声的测试
2. 显示识别结果和信置度
3. 交互模式，让你手动测试不同的声音

## 📖 API 文档 - API Documentation

### CatSoundRecognizer 类

#### 初始化
```python
recognizer = CatSoundRecognizer()
```

#### 方法

##### `recognize_sound(audio_data, sample_rate=16000)`
识别音频中的猫叫声

**参数:**
- `audio_data` (np.ndarray): 音频数据
- `sample_rate` (int): 采样率，默认 16000 Hz

**返回:**
```python
{
    'sound': str,           # 识别的声音类型
    'confidence': float,    # 信置度 (0-1)
    'emotion': str         # 推断的情感状态
}
```

**示例:**
```python
result = recognizer.recognize_sound(audio_data)
# {'sound': 'meow', 'confidence': 0.92, 'emotion': 'playful'}
```

---

##### `extract_features(audio_data, sample_rate=16000)`
提取音频特征

**参数:**
- `audio_data` (np.ndarray): 音频数据
- `sample_rate` (int): 采样率，默认 16000 Hz

**返回:**
```python
{
    'mfcc': np.ndarray,              # MFCC 系数
    'spectral_centroid': float,      # 频谱质心
    'zero_crossing_rate': float,     # 零交叉率
    'energy': float,                 # 音频能量
    'fundamental_freq': float        # 基频
}
```

---

##### `interpret_communication(sound)`
解释猫叫声的含义

**参数:**
- `sound` (str): 声音类型 ('meow', 'purr', 'hiss', 'growl', 'chirp', 'yowl')

**返回:**
- `str`: 包含中英双语的解释

**示例:**
```python
interpretation = recognizer.interpret_communication('purr')
# '猫咪很满足和放松 | Cat is satisfied and relaxed'
```

---

##### `get_response_suggestion(sound, emotion)`
获取对猫咪的推荐回应

**参数:**
- `sound` (str): 声音类型
- `emotion` (str): 情感状态

**返回:**
- `str`: 包含中英双语的建议

**示例:**
```python
suggestion = recognizer.get_response_suggestion('purr', 'happy')
# '轻轻抚摸猫咪，给予温暖 | Gently pet the cat and give warmth'
```

## 📊 音频特征说明 - Audio Features Explanation

### MFCC (Mel-Frequency Cepstral Coefficients)
- 模拟人类听觉系统对声音的感知
- 特别适合识别语音和动物声音

### 频谱质心 (Spectral Centroid)
- 表示频谱的「重心」位置
- 高频率内容多时值较高

### 零交叉率 (Zero Crossing Rate)
- 音频信号穿过零点的频率
- 用于区分有声和无声部分

### 基频 (Fundamental Frequency)
- 声音的最低频率分量
- 对应于人/动物声音的音调

## 💡 使用场景 - Use Cases

1. **宠物健康监控**: 识别猫的异常叫声，及时发现健康问题
2. **猫咪行为研究**: 分析猫咪的交流模式和行为
3. **智能家居集成**: 与智能家居系统集成，根据猫的需求自动调整环境
4. **宠物监护应用**: 开发宠物监护应用，帮助主人理解猫咪
5. **动物福利**: 在动物庇护所中使用，监控动物的福利状态

## 🔄 工作流程 - Workflow

```
音频输入
   ↓
特征提取 (MFCC, 频谱质心等)
   ↓
声音分类 (6 种猫叫声)
   ↓
情感推断
   ↓
生成建议
   ↓
输出结果
```

## 🎓 技术栈 - Technology Stack

- **numpy**: 数值计算
- **scipy**: 信号处理
- **scikit-learn**: 机器学习
- **librosa**: 音频分析
- **matplotlib**: 数据可视化

## 📝 示例输出 - Sample Output

```
==============================================================
🐱 猫语识别系统 - Cat Language Recognition System 🐱
==============================================================

🔊 测试声音: MEOW
   Testing sound: MEOW
   识别结果: MEOW
   Recognized as: MEOW
   信置度: 92.00%
   Confidence: 92.00%
   情感状态: playful
   Emotion: playful
   💬 解释: 猫咪想引起你的注意 | Cat wants your attention
   💬 Interpretation: 猫咪想引起你的注意 | Cat wants your attention
   💡 建议: 用玩具与猫咪互动 | Interact with the cat using toys
   💡 Suggestion: 用玩具与猫咪互动 | Interact with the cat using toys
```

## 🤝 贡献 - Contributing

欢迎提交 Issue 和 Pull Request！

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📄 许可证 - License

MIT License

## 👨‍💻 作者 - Author

Created with ❤️ for cat lovers everywhere

---

**提示**: 这是一个教学项目示例。实际的生产环境可能需要使用更复杂的机器学习模型和真实的训练数据。

**Note**: This is an educational project example. Production environments may require more complex machine learning models and real training data.
