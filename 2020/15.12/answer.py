def question(end):
    """
    Игра, в которой надо на каждом ходу называть числа.
    Начинаем с зачитывания стартовых цифр. Затем, на каждом ходу рассматриваются
    последние названные числа:
    - если число произнесено впервые, то текущий игрок говорит 0
    - в противном случае, текущий игрок называет число ходов,
    когда это число было произнесено ранее
    """
    inputs=[1,0,18,10,19,6]
    turn=0
    save_steps={}
    for step in inputs:
        save_steps[step]=turn
        turn+=1
    while turn<=end:
        
        previous=inputs[-1]
        #print(f"Turn {turn}: {previous}")
        if previous in save_steps.keys():
            inputs.append(turn-1-save_steps[previous])
        else:
            inputs.append(0)
        save_steps[previous]=turn-1
        turn+=1
    return previous
    
print(question(2020))
print(question(30000000))
