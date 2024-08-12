from app import create_app

def test_app_creation():
    """Test if the Flask app is created successfully."""
    app = create_app()
    assert app is not None
    assert isinstance(app.name, str)

def test_blueprint_registration():
    """Test if all blueprints are registered."""
    app = create_app()
    
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

def test_cors_headers():
    """Test if CORS headers are present in the response."""
    app = create_app()
    client = app.test_client()
    
    response = client.get('/')
    
    assert 'Access-Control-Allow-Origin' in response.headers, "CORS headers are not present"