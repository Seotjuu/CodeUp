# 1. [Branch란](https://backlog.com/git-tutorial/kr/stepup/stepup2_2.html)

## 1) branch는 한 작업자의 **work flow** 같은 것.
>
> commit = 한 작업, branch = 작업의 뭉치들을 한 작업자가 가져가서 분담하는 것
>
> > ex) 페이지 개발에서 메인 페이지 디자인 마무리됨.
> >
> > 1번 팀은 로그인 구현 --> 새로운 branch 분기하여 작업 후 main branch와 병합하여 작업 통합 (merge 작업)
> >
> > 2번 팀은 회원가입 구현 --> 새로운 branch 분기
>
## 2) commit은 특정 주제를 맡은 파트원들이 마음대로 조절 가능.
>
> > ex) 로그인 구현팀이 개발자 A,B,C로 이루어져있고 팀장은 A
> >
> > A가 B의 commit을 되돌리고 오류를 수정하라고 지시 가능
>
## 3) branch는 전체 총괄로 관리해야 함.
>
> > ex) 로그인 구현팀 팀장이 회원가입 팀의 branch를 변경할 수 없음.

# 2. Branch를 쉽게 이해하는 법

## 1) [시각화](https://github.com/tjrenffl8/CodeUp/network)
> 아래처럼 commit을 통해 branch가 생성되고 합병되는 것을 확인할 수 있음
>
> ![](https://lh3.googleusercontent.com/pw/AM-JKLVzGG52pDZ3rCLvUj8XbgQinv_JyMQ4Gy59EZb4ArRmo0st_D1a0RzF5l6Ch4bPmhfxGLxA3MjXAFXyCBD6TYRaFQ0Iv3D-sy8XErq51lxMgevAKW8sCVEq4qm4NfdGz8iaoZB17qwj2vPMQZvt0p1JzA=w945-h263-no)
>
> 파란색 branch가 노트북에서 생성된 branch, 중간에 흰색으로 자꾸들어가는 것은 내가 main branch로 합병한 것