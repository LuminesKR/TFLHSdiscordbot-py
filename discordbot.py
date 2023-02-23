from cmath import log
from discord.ext import commands
from distutils.sysconfig import PREFIX
import discord
import random
from dotenv import load_dotenv
import os
load_dotenv()


PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("놀방 인원들의 이야기를 들어주는중"))

@client.event
async def on_message(message):
    if message.content == "!안녕":
        await message.channel.send ("반가워요!")
       
    if message.content == "!기숙사":
        await message.channel.send ("1. 기숙사 입사 건강검진: 결핵(X-레이), 전염성 피부병 여부 포함 *(무조건 3월 2일까지 개학일에 담임 선생님께 제출하기 위해 가져오기)*

2. 입사일: 2023. 3. 2.(목)

3. 운영 방법: 매주 월요일 입사, 금요일 퇴사 (특별한 경우 직접 신청할 시 전날 일요일에 입사 가능할지 학교에서 의논중)

4. 방 배정 안내: 3. 2.(목) *등교 후* 학급별 안내 예정

5. 준비물: 이불, 여벌 옷, 세면도구, 목욕바구니, 수건, 개인 위생용품, 헤어드라이어 등

6. 입⚠금지⚠물품: 전자제품, 전열기, 고데기, 개인학습용 책상, 음식물(간식)

7. 전염병 및 식중독 예방을 위하여 기숙사 내에서는 음식물을 섭취할 수 없다.")

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
