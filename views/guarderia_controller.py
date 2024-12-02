from flask import Flask, render_template, jsonify, request
from models.Guarderia import Guarderia

def principal_routes(app):
    @app.route("/")
    def index():
            return render_template("index.html", animals=list(Guarderia.animals.keys()))
    
    @app.route("/animal/<string:nombre_animal>", methods=["GET"])
    def sonido_animal(nombre_animal):
        animal = Guarderia.animals.get(nombre_animal.lower())
        if not animal:
            if "application/json" in request.headers.get("Accept", ""):
                return jsonify({"error": "Animal no encontrado"}), 404
            return render_template("animal.html", error="Animal no encontrado"), 404
        
        if "application/json" in request.headers.get("Accept", ""):
            return jsonify({
                "animal": animal.nombre,
                "sonido": animal.hacer_sonido()
            })
        return render_template("animal.html", animal=animal)