import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
cred = credentials.Certificate("activate.json")

app = firebase_admin.initialize_app(cred, {
     'storageBucket': 'gs://easy-cloud-82e1a.appspot.com',
}, name='storage')

bucket = storage.bucket()
blob = bucket.getblob("Cui.png")
print(blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET'))