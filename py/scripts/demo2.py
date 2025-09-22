from spire.pdf import *
from spire.pdf.common import *

#PdfDocument 클래스의 인스턴스 생성
pdf = PdfDocument()

#PDF 문서 로드
pdf.LoadFromFile("Sample.pdf")

#이미지를 저장할 리스트 생성
images = []

#문서의 각 페이지를 반복
for i in range(pdf.Pages.Count):

    #페이지 가져오기
    page = pdf.Pages.get_Item(i)

    #페이지에서 이미지 추출하여 생성한 리스트에 저장
    for img in page.ExtractImages():
        images.append(img)

#리스트에 있는 이미지를 PNG 파일로 저장
i = 0
for image in images:
    i += 1
    image.Save("output/Images/Image-{0:d}.png".format(i), ImageFormat.get_Png())
pdf.Close()