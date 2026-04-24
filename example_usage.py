#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
项目标题: 🐱 猫语识别软件 - 使用示例
Title: Cat Language Recognition Software - Usage Example
================================================================================

项目描述:
    这是猫语识别系统的完整使用示例程序。
    演示了如何识别6种不同的猫叫声，推断猫的情感状态，
    并提供相应的互动建议。

Description:
    This is a complete usage example program for the cat language recognition system.
    It demonstrates how to recognize 6 different cat sounds, infer emotional states,
    and provide interaction recommendations.

功能 (Features):
    ✅ 生成不同类型的猫叫声示例
    ✅ 演示识别系统的完整工作流程
    ✅ 交互式模式让用户手动测试
    ✅ 详细显示识别结果和建议

使用方式 (Usage):
    python example_usage.py

================================================================================
"""

import numpy as np
from cat_sound_recognizer import CatSoundRecognizer

def generate_sample_audio(sound_type='meow', duration=1.0, sample_rate=16000):
    """
    🎵 生成示例音频数据
    Generate sample audio data for testing
    
    根据指定的叫声类型生成模拟音频数据。
    
    Args:
        sound_type (str): 叫声类型 - 'meow', 'purr', 'hiss', 'growl', 'chirp', 'yowl'
        duration (float): 音频时长，单位秒 (seconds)
        sample_rate (int): 采样率 (Hz)
    
    Returns:
        np.ndarray: 生成的音频数据数组
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
    
    # 添加噪声以增加真实感
    audio += np.random.randn(len(audio)) * 0.05
    
    return audio

def main():
    """
    🎯 主程序
    Main program entry point
    
    运行完整的演示和交互式测试。
    """
    print("="*70)
    print("🐱 猫语识别系统 - Cat Language Recognition System 🐱")
    print("="*70)
    print()
    print("📖 项目描述 Project Description:")
    print("   一个能够识别和解释猫叫声及其情感状态的智能系统")
    print("   An intelligent system that recognizes and interprets cat sounds and emotions")
    print()
    
    # 初始化识别器
    recognizer = CatSoundRecognizer()
    
    # 测试所有猫叫声类型
    test_sounds = ['meow', 'purr', 'hiss', 'growl', 'chirp', 'yowl']
    
    print("📊 自动演示 - Automatic Demonstration:")
    print("-" * 70)
    
    for sound_type in test_sounds:
        print(f"\n🔊 测试叫声: {sound_type.upper()}")
        print(f"   Testing sound: {sound_type.upper()}")
        print(f"   {'-'*65}")
        
        # 生成示例音频
        audio_data = generate_sample_audio(sound_type)
        
        # 识别叫声
        result = recognizer.recognize_sound(audio_data)
        
        # 解释交流意图
        interpretation = recognizer.interpret_communication(result['sound'])
        
        # 获取推荐回应
        suggestion = recognizer.get_response_suggestion(
            result['sound'], 
            result['emotion']
        )
        
        # 输出结果
        print(f"   ✅ 识别结果 Recognition Result: {result['sound'].upper()}")
        print(f"   📈 信置度 Confidence: {result['confidence']:.2%}")
        print(f"   😸 情感状态 Emotional State: {result['emotion']}")
        print(f"   💬 含义 Meaning: {interpretation}")
        print(f"   💡 建议 Suggestion: {suggestion}")
    
    print("\n" + "="*70)
    print("✅ 自动演示完成 - Automatic Demonstration Complete")
    print("="*70)
    
    # 交互模式
    print("\n🎮 交互模式 - Interactive Mode:")
    print("-" * 70)
    
    while True:
        print("\n📌 可用的猫叫声类型 Available cat sounds:")
        print("   meow | purr | hiss | growl | chirp | yowl")
        print()
        
        user_input = input("请输入叫声类型 (或 'quit' 退出) / Enter sound type (or 'quit' to exit): ").strip().lower()
        
        if user_input == 'quit':
            print("\n👋 再见! 希望你的猫咪一切安好!")
            print("   Goodbye! Hope your cat is well!")
            break
        
        if user_input not in test_sounds:
            print("❌ 无效的输入。请选择有效的猫叫声类型。")
            print("   Invalid input. Please select a valid cat sound.")
            continue
        
        # 生成和识别
        audio_data = generate_sample_audio(user_input)
        result = recognizer.recognize_sound(audio_data)
        interpretation = recognizer.interpret_communication(result['sound'])
        suggestion = recognizer.get_response_suggestion(result['sound'], result['emotion'])
        
        print(f"\n✨ 识别结果 Recognition Results:")
        print(f"   🔊 叫声类型 Sound Type: {result['sound'].upper()}")
        print(f"   📈 信置度 Confidence: {result['confidence']:.2%}")
        print(f"   😸 情感 Emotion: {result['emotion']}")
        print(f"   💬 解释 Interpretation: {interpretation}")
        print(f"   💡 建议 Suggestion: {suggestion}")
        print(f"   {'-'*65}")

if __name__ == '__main__':
    main()
