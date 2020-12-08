from shorty.app import create_app

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# create the application 
app = create_app()

# run it 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~