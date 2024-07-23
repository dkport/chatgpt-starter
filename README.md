# ChatGPT Starter

## Overview

This project provides a basic interface for working with chatgpt. 
The main entry point for the system is `chat` bash script located in the `bin` directory.

## Requirements

- python 3.x
- openai

## Installation


1. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install the required dependencies:
    ```sh
    pip install --upgrade -r requirements.txt
    ```

## Usage

To see how to run the system, use:

```sh
bin/chat -h
```

To see all commands that Makefile process, run:
```sh
make all
```

To run unittests, use:
```sh
make test
```

To clean from python cache, run:
```sh
make clean
```
