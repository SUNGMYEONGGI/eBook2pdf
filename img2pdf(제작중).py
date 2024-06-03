import img2pdf
import os

def images_to_pdf(image_folder, output_pdf):
    # 이미지 파일 목록 가져오기
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # 이미지 파일들을 정렬
    image_files.sort()

    # 이미지 파일들을 PDF로 변환
    with open(output_pdf, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert([os.path.join(image_folder, f) for f in image_files]))

# 예시: 이미지 파일이 있는 폴더와 출력 PDF 파일 지정
image_folder = "pdf_images"
output_pdf = "output.pdf"

# 이미지 파일들을 PDF로 변환
images_to_pdf(image_folder, output_pdf)

print("PDF 변환 완료!")