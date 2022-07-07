FROM ubuntu:20.04
RUN ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime \
    && echo "Etc/UTC" > /etc/timezone \
    && apt-get update && apt-get upgrade -y \
    && apt-get install -y python3 texlive-latex-base texlive-fonts-recommended texlive-latex-extra

COPY sections/ /sections/
COPY configureCV.py /configureCV.py
COPY createCV.py /createCV.py

CMD [ "python3","createCV.py" ]