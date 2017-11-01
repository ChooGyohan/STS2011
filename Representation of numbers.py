#20160458 추교한

def expressions(num):
    answer = 0
    for x in range(1,num+1) :
        sum=0
        for y in range(x,num+1) :
            sum += y
            if sum == num :
                answer += 1
                break

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15));
