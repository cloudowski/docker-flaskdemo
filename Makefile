NAME = cloudowski/flaskdemo
DOCKER_CMD = docker

.PHONY: all build push

all: build

build: .build-0.1 .build-0.2 .build-0.3

.build-%:
		$(DOCKER_CMD) build --build-arg SRC=versions/$* -t $(NAME):$* .


push:
		$(DOCKER_CMD) push $(NAME)
