from flask import Flask

from blueprints.simulator.simulator import SimulatorBP

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    with app.app_context():

        simulator_bp = SimulatorBP()
        
        app.register_blueprint(simulator_bp.simulator_bp)
        return app
        
if __name__ == "__main__":
    app = init_app()
    app.run(debug=True, port=5004)