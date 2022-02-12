# Uncomment if you want to load variables from .env file
# include ./.env
# export $(shell sed 's/=.*//' ./.env)

NAME   := 'finloop/shap-emotions-correction-api'
TAG    := $(shell git log -1 --pretty=format:"%h")
IMG    := ${NAME}:${TAG}
LATEST := ${NAME}:latest


build:
	@docker build -t ${IMG} .
	@docker tag ${IMG} ${LATEST}

# Run: 'make login' or 'docker login'
# before trying to push
push:
	@docker push ${NAME}

login:
	@docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}