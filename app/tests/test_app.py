from app import app

def test_healthz():
    with app.test_client() as c:
        rv = c.get('/healthz')
        assert rv.status_code == 200
        assert rv.json['status'] == 'ok'
