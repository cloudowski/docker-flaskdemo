NAME = cloudowski/flaskdemo
DOCKER_CMD = docker

.PHONY: all build push

all: build

build:
		$(DOCKER_CMD) build --build-arg SRC=versions/0.1 -t $(NAME):0.1 .
		$(DOCKER_CMD) build --build-arg SRC=versions/0.2 -t $(NAME):0.2 .
		$(DOCKER_CMD) build --build-arg SRC=versions/0.3 -t $(NAME):0.3 .

push:
		$(DOCKER_CMD) push $(NAME)
