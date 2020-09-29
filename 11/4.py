def get_scores():
    scores = input('Enter scores separated by space: ')
    score_list = [float(i) for i in scores.split()]
    
    return score_list

def process_list(score_list):
    for i in range (2):
        score_list.remove(min(score_list))
    
    return sum(score_list)
    
        

def output(sum_of_scores):
    print('Sum of scores (two lowest removed): {}'.format(sum_of_scores))

def main():
    score_list = get_scores()
    if len(score_list) < 2:
        print('At least two scores needed!')
    else:
        sum_of_scores = process_list(score_list)
        
    output(sum_of_scores)

main()