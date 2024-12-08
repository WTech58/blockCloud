APP_DIR = src/app
JSON_FILE = $(APP_DIR)/bc.json
REQUIRED_PACKAGES = flask

PYTHON_URL_LINUX = https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz
PYTHON_URL_WINDOWS = https://www.python.org/ftp/python/3.10.4/python-3.10.4.exe

.PHONY: init check_json check_python download_python clean

init: check_json check_python

check_json:
	@if [ ! -f $(JSON_FILE) ]; then \
		echo "建立 $(JSON_FILE)..."; \
		touch $(JSON_FILE); \
	else \
		echo "JSON文件 $(JSON_FILE) 已經存在."; \
	fi

check_python:
	@command -v python3 >/dev/null 2>&1 || { \
		echo "Python3 沒有安裝. 自動安裝中..."; \
		$(MAKE) download_python; \
		exit 1; \
	}
	@echo "Python3 is installed."
	@for package in $(REQUIRED_PACKAGES); do \
		pip show $$package >/dev/null 2>&1 || { \
			echo "沒有 $$package. 自動安裝中..."; \
			pip install $$package; \
		}; \
		echo " $$package 已經存在."; \
	done

download_python:
	@echo "分析 OS..."
	@OS := $(shell uname -s)
	@if [ "$$OS" = "Linux" ]; then \
		echo "下載 Python Linux版..."; \
		wget $(PYTHON_URL_LINUX) -O Python.tgz; \
		tar -xzf Python.tgz; \
		cd Python-* && ./configure && make && sudo make install; \
	else \
		echo "下載 Python Windows版..."; \
		wget $(PYTHON_URL_WINDOWS) -O python-installer.exe; \
		echo "請執行 python-installer.exe 去安裝 Python."; \
	fi

clean:
	rm -f $(JSON_FILE) Python.tgz python-installer.exe
