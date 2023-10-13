FROM hitokizzy/geezram:slim-buster

RUN git clone -b main https://github.com/ezbw69/geez /home/geez/
WORKDIR /home/geez

RUN wget https://raw.githubusercontent.com/ezbw69/geez/main/requirements.txt \
    && pip3 install --no-cache-dir -U -r requirements.txt \
    && rm requirements.txt
    
CMD bash start
