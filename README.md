crud 프로젝트 시작

movie 앱 만들기

path("", views.list, name="list"), # 리스트 인덱스 
path("new/", views.new, name="new"),   # create url
path("<int:id>/", views.detail, name="detail"), # 리드 디테일
path("<int:id>/update/", views.update, name="update"), # 업데이트
path("<int:id>/delete/", views.delete, name="delete"), # 삭제

path("<int:id>/comment/", views.comment, name="comment"), #댓글 코멘트


부트스트랩 적용

모델링 - Movie, Comment 두가지

views - new, detail, update, delete, comment 함수 활용
2가지 합쳐서 적용시켰습니다.