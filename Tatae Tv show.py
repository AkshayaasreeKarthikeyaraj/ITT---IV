import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    num_test_cases = int(input_data[0])
    current_index = 1
    results = []
    
    for _ in range(num_test_cases):
        n = int(input_data[current_index])
        k = int(input_data[current_index + 1])
        s = input_data[current_index + 2]
        current_index += 3
        
        remainder_counts = [0] * k
        for i, char in enumerate(s):
            if char == '1':
                remainder_counts[i % k] += 1
        
        is_possible = True
        for count in remainder_counts:
            if count % 2 != 0:
                is_possible = False
                break
        
        if is_possible:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
