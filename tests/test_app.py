def test_app_creation(app):
    assert app is not None
    assert isinstance(app.name, str)

def test_blueprint_registration(app):
    expected_blueprints = [
        'gemini_bp',
        'trademark_bp',
        'sd_bp',
        'gt_bp',
        'firebase_bp',
        'etsy_bp'
    ]
   
    registered_blueprints = [bp.name for bp in app.blueprints.values()]
   
    for bp in expected_blueprints:
        assert bp in registered_blueprints, f"Blueprint {bp} is not registered"

def test_cors_headers(client):
    response = client.get('/')
   
    assert 'Access-Control-Allow-Origin' in response.headers, "CORS headers are not present"