#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
猫语识别软件 - 使用示例
Cat Language Recognition - Usage Example
"""

import numpy as np
from cat_sound_recognizer import CatSoundRecognizer

def generate_sample_audio(sound_type='meow', duration=1.0, sample_rate=16000):
    """
    生成示例音频数据 - Generate sample audio data
    """
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    if sound_type == 'meow':
        # 模拟Meow声：中等频率，短脉冲
        freq = 800
        audio = np.sin(2 * np.pi * freq * t)
    elif sound_type == 'purr':
        # 模拟Purr声：低频，连续
        freq = 150
        audio = np.sin(2 * np.pi * freq * t) * 0.3
    elif sound_type == 'hiss':
        # 模拟Hiss声：高频，噪声
        audio = np.random.randn(len(t)) * 0.5
    elif sound_type == 'growl':
        # 模拟Growl声：低中频
        freq = 300
        audio = np.sin(2 * np.pi * freq * t) * 0.4
    elif sound_type == 'chirp':
        # 模拟Chirp声：上升频率
        freq_start, freq_end = 1000, 2000
        freq = np.linspace(freq_start, freq_end, len(t))
        audio = np.sin(2 * np.pi * freq * t) * 0.3
    else:  # yowl
        # 模拟Yowl声：长的、高的声音
        freq = 600
        audio = np.sin(2 * np.pi * freq * t) * 0.4
    
    # 添加噪声
    audio += np.random.randn(len(audio)) * 0.05
    
    return audio

def main():
    print("="*60)
    print("🐱 猫语识别系统 - Cat Language Recognition System 🐱")
    print("="*60)
    print()
    
    # 初始化识别器
    recognizer = CatSoundRecognizer()
    
    # 测试所有猫叫声类型
    test_sounds = ['meow', 'purr', 'hiss', 'growl', 'chirp', 'yowl']
    
    print("\n📊 识别结果 - Recognition Results:")
    print("-" * 60)
    
    for sound_type in test_sounds:
        print(f"\n🔊 测试声音: {sound_type.upper()}")
        print(f"   Testing sound: {sound_type.upper()}")
        
        # 生成示例音频
        audio_data = generate_sample_audio(sound_type)
        
        # 识别声音
        result = recognizer.recognize_sound(audio_data)
        
        # 解释交流意图
        interpretation = recognizer.interpret_communication(result['sound'])
        
        # 获取推荐回应
        suggestion = recognizer.get_response_suggestion(
            result['sound'], 
            result['emotion']
        )
        
        # 输出结果
        print(f"   识别结果: {result['sound'].upper()}")
        print(f"   Recognized as: {result['sound'].upper()}")
        print(f"   信置度: {result['confidence']:.2%}")
        print(f"   Confidence: {result['confidence']:.2%}")
        print(f"   情感状态: {result['emotion']}")
        print(f"   Emotion: {result['emotion']}")
        print(f"   💬 解释: {interpretation}")
        print(f"   💬 Interpretation: {interpretation}")
        print(f"   💡 建议: {suggestion}")
        print(f"   💡 Suggestion: {suggestion}")
    
    print("\n" + "="*60)
    print("✅ 识别完成 - Recognition Complete")
    print("="*60)
    
    # 交互模式
    print("\n🎮 交互模式 - Interactive Mode:")
    print("-" * 60)
    
    while True:
        print("\n可用的猫叫声: meow, purr, hiss, growl, chirp, yowl")
        print("Available sounds: meow, purr, hiss, growl, chirp, yowl")
        
        user_input = input("\n请输入猫叫声类型 (或 'quit' 退出): ").strip().lower()
        
        if user_input == 'quit':
            print("\n👋 再见! 希望你的猫咪一切安好! | Goodbye! Hope your cat is well!")
            break
        
        if user_input not in test_sounds:
            print("❌ 无效的输入。请选择有效的猫叫声类型。")
            print("❌ Invalid input. Please select a valid cat sound.")
            continue
        
        audio_data = generate_sample_audio(user_input)
        result = recognizer.recognize_sound(audio_data)
        interpretation = recognizer.interpret_communication(result['sound'])
        suggestion = recognizer.get_response_suggestion(result['sound'], result['emotion'])
        
        print(f"\n✨ 识别结果:")
        print(f"   声音类型: {result['sound'].upper()}")
        print(f"   信置度: {result['confidence']:.2%}")
        print(f"   情感: {result['emotion']}")
        print(f"   解释: {interpretation}")
        print(f"   建议: {suggestion}")

if __name__ == '__main__':
    main()
