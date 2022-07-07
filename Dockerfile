FROM ubuntu:20.04
RUN apt-get -y update && apt-get install -y python3 texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra

COPY sections/ /sections/
COPY configureCV.py /configureCV.py
COPY createCV.py /createCV.py

CMD [ "python3","createCV.py" ]