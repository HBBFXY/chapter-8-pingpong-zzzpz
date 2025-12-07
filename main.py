import random

def simulate_single_game(prob_a):
    score_a = 0
    score_b = 0
    while True:
        if random.random() < prob_a:
            score_a += 1
        else:
            score_b += 1
        
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return 'A' if score_a > score_b else 'B'

def simulate_single_match(prob_a, best_of=3):
    wins_a = 0
    wins_b = 0
    while wins_a < (best_of+1)//2 and wins_b < (best_of+1)//2:
        winner = simulate_single_game(prob_a)
        if winner == 'A':
            wins_a += 1
        else:
            wins_b += 1
    return 'A' if wins_a > wins_b else 'B'

def analyze_competition(prob_a, num_matches, best_of=3):
    wins_a_total = 0
    for _ in range(num_matches):
        winner = simulate_single_match(prob_a, best_of)
        if winner == 'A':
            wins_a_total += 1
    print(f"模拟{num_matches}场比赛（{best_of}局{((best_of+1)//2)}胜制）：")
    print(f"A选手获胜概率：{prob_a:.2f}")
    print(f"A实际获胜场数：{wins_a_total}，胜率：{wins_a_total/num_matches:.2%}")
    print(f"B实际获胜场数：{num_matches - wins_a_total}，胜率：{(num_matches - wins_a_total)/num_matches:.2%}")

if __name__ == "__main__":
    analyze_competition(prob_a=0.55, num_matches=1000, best_of=3)
