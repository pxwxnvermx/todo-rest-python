import uvicorn


def main():
    uvicorn.run("app:app", host='localhost', port=3000, reload=True, debug=True, workers=3)


if __name__ == '__main__':
    main()
