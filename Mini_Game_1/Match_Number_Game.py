# TODO step0
ENV_TITLE_MAX_LEN = 20
ENV_PNAME_MAX_LEN = 15
VERSION = "V 1.0"

# TODO step1
# 게임이 시작하면 Enjoy Custom Game World"라는 문구가 출력된다
game_start_prompt = 'Enjoy Custom Game World'
print( game_start_prompt )

# TODO step2
'''
- "게임 제목을 입력하세요, 단 20자 이내로 입력 가능합니다." 
 라는 문구가 출력된다
- 플레이어가 입력할때까지 무제한으로 대기한다
- 아무것도 입력하지 않고 엔터를 치면(조건1) "정확하게 입력하세요" 라고 출력하고 
  다시 입력 대기한다
- 20자 이상 입력하고 엔터를 치면(조건2), "20자가 초과되었습니다." 라고 출력하고,
  다시 입력 대기한다.
- 20자 이내로 입력하고 엔터를 치면(조건3) gameTitle이라는 변수에 게임 제목을
  담고 다음 단계로 이동한다 -> 반복문을 빠져나간다
'''
gameTitle = None
if not gameTitle:
  msg = f"게임 제목을 입력하세요, 단 {ENV_TITLE_MAX_LEN}자 이내로 입력 가능합니다.: "
  while True:
      gameTitle = input(msg).strip()
      if not gameTitle:
        print("정확하게 입력하세요")
        continue      
      elif len(gameTitle) > ENV_TITLE_MAX_LEN:
        print(str(ENV_TITLE_MAX_LEN) + "자가 초과되었습니다.")
        continue
      break

  print( '게임 제목은: ', gameTitle )

# TODO step3
'''
- 플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
- 입력에 대한 체크 포인트는 Step2와 동일하다
- 플레이어에 대한 닉네임은 player_name이라는 변수에 보관한다
'''
player_name = None
msg         = "플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다: "  % ENV_PNAME_MAX_LEN
while not player_name:
  tmp         = input(msg).strip()
  if not tmp:
    print('정확하게 입력하세요')
    pass
  elif len(tmp) > ENV_PNAME_MAX_LEN:
    print( '닉네임은 {}자 이내로 입력하세요'.format(ENV_PNAME_MAX_LEN) )
    pass
  else:
    player_name = tmp
    break

print('플레이어의 닉네임: ', player_name)

# TODO step4
'''
------------------------------
-         게임 제목          -
-          v 1.0             -
-   welcome 플레어이름       - 
------------------------------
'''

p_max_len = 2 + 2 + 1 + len('welcome') + ENV_PNAME_MAX_LEN

print( '-'*p_max_len )
print(f'-{gameTitle:^25}-')
print(f'-{VERSION:^25}-')
print(f'-{"welcome "+player_name:^25}-')
print( '-'*p_max_len )
print('\n 게임이 시작됩니다. AI가 숫자를 준비합니다. \n')

# TODO Step5

# TODO Step6
