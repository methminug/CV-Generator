FROM ubuntu:latest

RUN ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime \
    && echo "Etc/UTC" > /etc/timezone \
    && apt-get update && apt-get upgrade -y \
    && apt-get install python3 texlive-latex-base texlive-xetex texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra xzdec -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /data

COPY script.sh /script.sh
COPY sections/ /sections/
COPY configureCV.py /configureCV.py
COPY createCV.py /createCV.py

RUN chmod +x script.sh