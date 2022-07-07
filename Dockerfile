FROM ubuntu:latest

RUN ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime \
    && echo "Etc/UTC" > /etc/timezone \
    && apt-get update && apt-get upgrade -y \
    && apt-get install python3 texlive-latex-base texlive-xetex texlive-latex-extra texlive-fonts-recommended xzdec -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /data

COPY sections/ /sections/
COPY configureCV.py /configureCV.py
COPY createCV.py /createCV.py

CMD [ "python3","createCV.py" ]
ENTRYPOINT [ "/bin/sh", "-c", "xelatex -output-directory=generatedpdf cv.tex"]