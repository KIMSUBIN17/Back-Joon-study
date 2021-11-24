word = input()
alpha = list(range(97,123))

for x in alpha :
    print(word.find(chr(x)))


#문제
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

#해설
a~z까지 알파벳은 아스키코드의 숫자범위로 리스트를 생성함
a=97 z=122

find() : 어떤 문자가 문자열 안에서 첫번째에 위치한 순서를 숫자로 출력, 문자열안에 없으면 -1 출력 / 문자열에서만 가능. 
cf) index() : 문자열 뿐 아니라 리스트,튜플 등 반복 가능한 iterable 자료형에서도 찾는 문자의 인덱스 반환하는 함수로 쓰임
차이점)find함수는 찾는 문자가 문자열 안에 없으면 -1 출력. 
index()는 AttributeError 발생

chr() : 숫자(아스키코드) -> 문자 변환
ord() : 문자 -> 숫자(아스키코드)

