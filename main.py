from website import create_app

app = create_app()

if __name__=='__main__':#This means server runs if you access this file directly
    app.run(debug=True) 