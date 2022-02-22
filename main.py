import uvicorn


def main():
    uvicorn.run("app:app", host='localhost', port=5000, reload=True, debug=True, workers=3)


if __name__ == '__main__':
    main()
