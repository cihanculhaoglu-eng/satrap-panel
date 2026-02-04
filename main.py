from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# Geçici veri (Excel gibi)
records = []

@app.get("/", response_class=HTMLResponse)
def home():
    rows = ""
    for r in records:
        rows += f"""
        <tr>
            <td>{r['tarih']}</td>
            <td>{r['firma']}</td>
            <td>{r['urun']}</td>
            <td>{r['gtip']}</td>
            <td>{r['miktar']}</td>
            <td>{r['ulke']}</td>
            <td>{r['gumruk']}</td>
            <td>{r['not']}</td>
        </tr>
        """

    return f"""
    <html>
    <head>
        <title>İthalat Paneli</title>
    </head>
    <body>
        <h2>İthalat Tablosu</h2>

        <form method="post" action="/ekle">
            Tarih: <input name="tarih"><br>
            Firma: <input name="firma"><br>
            Ürün: <input name="urun"><br>
            GTİP: <input name="gtip"><br>
            Miktar: <input name="miktar"><br>
            Ülke: <input name="ulke"><br>
            Gümrük: <input name="gumruk"><br>
            Not: <input name="not"><br><br>
            <button type="submit">Kaydet</button>
        </form>

        <br><br>

        <table border="1" cellpadding="5">
            <tr>
                <th>Tarih</th><th>Firma</th><th>Ürün</th><th>GTİP</th>
                <th>Miktar</th><th>Ülke</th><th>Gümrük</th><th>Not</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """


@app.post("/ekle")
def ekle(
    tarih: str = Form(...),
    firma: str = Form(...),
    urun: str = Form(...),
    gtip: str = Form(...),
    miktar: str = Form(...),
    ulke: str = Form(...),
    gumruk: str = Form(...),
    not: str = Form(...)
):
    records.append({
        "tarih": tarih,
        "firma": firma,
        "urun": urun,
        "gtip": gtip,
        "miktar": miktar,
        "ulke": ulke,
        "gumruk": gumruk,
        "not": not
    })
    # Kayıt sonrası anasayfaya dön
    return RedirectResponse(url="/", status_code=303)
