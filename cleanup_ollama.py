#!/usr/bin/env python3
"""
Cleanup script to stop unnecessary Ollama processes
Run this if you notice high CPU usage from Ollama
"""

import subprocess
import sys
import time

def stop_ollama_processes():
    """Stop all Ollama processes to free up resources"""
    try:
        print("🔄 Stopping Ollama processes...")
        
        # On Windows
        if sys.platform == "win32":
            result = subprocess.run(
                ["taskkill", "/f", "/im", "ollama.exe"], 
                capture_output=True, 
                text=True
            )
            if result.returncode == 0:
                print("✅ Ollama processes stopped successfully")
            else:
                print("ℹ️  No Ollama processes found or already stopped")
        else:
            # On Unix-like systems
            result = subprocess.run(
                ["pkill", "-f", "ollama"], 
                capture_output=True, 
                text=True
            )
            if result.returncode == 0:
                print("✅ Ollama processes stopped successfully")
            else:
                print("ℹ️  No Ollama processes found or already stopped")
                
    except Exception as e:
        print(f"❌ Error stopping Ollama processes: {e}")

def check_system_resources():
    """Check current system resource usage"""
    try:
        import psutil
        
        print("\n📊 Current System Resources:")
        print(f"CPU Usage: {psutil.cpu_percent(interval=1):.1f}%")
        print(f"Memory Usage: {psutil.virtual_memory().percent:.1f}%")
        
        # Check for Ollama processes
        ollama_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                if 'ollama' in proc.info['name'].lower():
                    ollama_processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        if ollama_processes:
            print(f"\n🔍 Found {len(ollama_processes)} Ollama processes:")
            for proc in ollama_processes:
                print(f"  PID {proc['pid']}: {proc['name']} (CPU: {proc['cpu_percent']:.1f}%, Memory: {proc['memory_percent']:.1f}%)")
        else:
            print("\n✅ No Ollama processes found")
            
    except ImportError:
        print("ℹ️  Install psutil to see detailed resource usage: pip install psutil")
    except Exception as e:
        print(f"❌ Error checking resources: {e}")

if __name__ == "__main__":
    print("🧹 Ollama Cleanup Tool")
    print("=" * 30)
    
    check_system_resources()
    
    response = input("\n❓ Do you want to stop all Ollama processes? (y/N): ").strip().lower()
    if response in ['y', 'yes']:
        stop_ollama_processes()
        time.sleep(2)
        check_system_resources()
    else:
        print("ℹ️  No changes made")

