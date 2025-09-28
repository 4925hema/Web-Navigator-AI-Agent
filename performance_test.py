#!/usr/bin/env python3
"""
Performance test script for the web navigator agent
Run this to benchmark the improvements
"""

import time
import psutil
import os
from app.agent_main import agent

def get_memory_usage():
    """Get current memory usage in MB"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024

def test_performance():
    """Test the agent performance with sample queries"""
    print("🧪 Performance Test Starting...")
    print(f"📊 Initial Memory Usage: {get_memory_usage():.2f} MB")
    
    test_queries = [
        "search for laptops on amazon",
        "find mobile phones on flipkart", 
        "search for python programming books"
    ]
    
    total_time = 0
    results = []
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n🔄 Test {i}/3: {query}")
        start_time = time.time()
        start_memory = get_memory_usage()
        
        try:
            result = agent.invoke({"input": query})
            end_time = time.time()
            end_memory = get_memory_usage()
            
            duration = end_time - start_time
            memory_used = end_memory - start_memory
            
            results.append({
                'query': query,
                'duration': duration,
                'memory_used': memory_used,
                'success': True
            })
            
            print(f"✅ Completed in {duration:.2f}s (Memory: +{memory_used:.2f} MB)")
            total_time += duration
            
        except Exception as e:
            end_time = time.time()
            duration = end_time - start_time
            results.append({
                'query': query,
                'duration': duration,
                'memory_used': 0,
                'success': False,
                'error': str(e)
            })
            print(f"❌ Failed in {duration:.2f}s: {e}")
    
    # Summary
    print(f"\n📈 Performance Summary:")
    print(f"Total Time: {total_time:.2f}s")
    print(f"Average Time: {total_time/len(test_queries):.2f}s")
    print(f"Success Rate: {sum(1 for r in results if r['success'])}/{len(results)}")
    print(f"Final Memory Usage: {get_memory_usage():.2f} MB")
    
    return results

if __name__ == "__main__":
    test_performance()

