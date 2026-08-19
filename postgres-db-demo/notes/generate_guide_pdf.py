"""Generate a generic PDF guide for the postgres-db-demo folder structure."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

NAVY = colors.HexColor("#1B365D")
BLUE = colors.HexColor("#2457C5")
LIGHT = colors.HexColor("#F3F6FB")
CODE_BG = colors.HexColor("#F7F8FA")
LINE = colors.HexColor("#D9E0EA")
MUTED = colors.HexColor("#4B5565")
WHITE = colors.white
OUT = Path(__file__).with_name("FastAPI-Product-API-Guide.pdf")


def styles():
    base = getSampleStyleSheet()
    return {
        "cover_sub": ParagraphStyle(
            "cover_sub", parent=base["Normal"], fontName="Times-Italic",
            fontSize=13, leading=18, textColor=MUTED, alignment=TA_CENTER, spaceAfter=6,
        ),
        "h1": ParagraphStyle(
            "h1", parent=base["Heading1"], fontName="Times-Bold",
            fontSize=16, leading=20, textColor=NAVY, spaceBefore=14, spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "h2", parent=base["Heading2"], fontName="Times-Bold",
            fontSize=13, leading=17, textColor=BLUE, spaceBefore=10, spaceAfter=6,
        ),
        "body": ParagraphStyle(
            "body", parent=base["Normal"], fontName="Times-Roman",
            fontSize=10.5, leading=15, textColor=colors.HexColor("#1F2933"),
            alignment=TA_JUSTIFY, spaceAfter=6,
        ),
        "callout": ParagraphStyle(
            "callout", parent=base["Normal"], fontName="Times-Roman",
            fontSize=10.5, leading=15, textColor=NAVY,
        ),
        "note": ParagraphStyle(
            "note", parent=base["Normal"], fontName="Times-Italic",
            fontSize=10.5, leading=15, textColor=MUTED, spaceAfter=6,
        ),
        "small": ParagraphStyle(
            "small", parent=base["Normal"], fontName="Times-Roman",
            fontSize=9, leading=12, textColor=MUTED,
        ),
        "th": ParagraphStyle(
            "th", parent=base["Normal"], fontName="Times-Bold",
            fontSize=9.5, leading=13, textColor=WHITE, alignment=TA_CENTER,
        ),
        "td": ParagraphStyle(
            "td", parent=base["Normal"], fontName="Times-Roman",
            fontSize=9.5, leading=13, textColor=colors.HexColor("#1F2933"),
        ),
        "code": ParagraphStyle(
            "code", parent=base["Code"], fontName="Courier",
            fontSize=8, leading=10.5, textColor=colors.HexColor("#111827"),
            backColor=CODE_BG,
        ),
    }


S = styles()


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, A4[1] - 14 * mm, A4[0], 14 * mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Times-Bold", 9)
    canvas.drawString(18 * mm, A4[1] - 9 * mm, "FastAPI Product API  |  Folder structure, routes, and how to run")
    canvas.setFillColor(LINE)
    canvas.rect(0, 12 * mm, A4[0], 0.4, fill=1, stroke=0)
    canvas.setFillColor(MUTED)
    canvas.setFont("Times-Roman", 8)
    canvas.drawString(18 * mm, 7 * mm, "Generic course notes  |  postgres-db-demo")
    canvas.drawRightString(A4[0] - 18 * mm, 7 * mm, f"Page {doc.page}")
    canvas.restoreState()


def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, A4[1] - 42 * mm, A4[0], 42 * mm, fill=1, stroke=0)
    canvas.setFillColor(BLUE)
    canvas.rect(0, A4[1] - 45 * mm, A4[0], 3 * mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Times-Bold", 11)
    canvas.drawCentredString(A4[0] / 2, A4[1] - 18 * mm, "BACKEND NOTES")
    canvas.setFont("Times-Bold", 20)
    canvas.drawCentredString(A4[0] / 2, A4[1] - 28 * mm, "How a real FastAPI project is organised")
    canvas.setFont("Times-Roman", 12)
    canvas.drawCentredString(A4[0] / 2, A4[1] - 36 * mm, "Folders  •  Routes  •  requirements.txt  •  How to run")
    header_footer(canvas, doc)
    canvas.restoreState()


def p(text, style="body"):
    return Paragraph(text, S[style])


def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(i, S["body"]), leftIndent=8, bulletColor=BLUE) for i in items],
        bulletType="bullet",
        start="circle",
        leftIndent=16,
        bulletFontName="Times-Roman",
        bulletFontSize=9,
        spaceAfter=6,
    )


def callout(title, text):
    data = [[Paragraph(f"<b>{title}</b><br/>{text}", S["callout"])]]
    t = Table(data, colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.6, BLUE),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def code_block(text):
    data = [[Preformatted(text.strip("\n"), S["code"])]]
    t = Table(data, colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("BOX", (0, 0), (-1, -1), 0.4, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def table(headers, rows, widths=None):
    if widths is None:
        widths = [170 * mm / len(headers)] * len(headers)
    data = [[Paragraph(h, S["th"]) for h in headers]]
    for row in rows:
        data.append([Paragraph(c, S["td"]) for c in row])
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.3, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def spacer(h=4):
    return Spacer(1, h * mm)


def build():
    story = []
    story.append(Spacer(1, 48 * mm))
    story.append(p("A simple Product CRUD API using FastAPI, PostgreSQL, and cursor SQL", "cover_sub"))
    story.append(spacer(4))
    story.append(callout(
        "One idea for the whole document",
        "Do not put everything in one main.py. Split the work: URL, JSON check, SQL, database connection. "
        "Companies do this so many people can work on the same project without breaking each other.",
    ))

    story.append(p("1. Why folders like a real company project", "h1"))
    story.append(p(
        "In a first program, all code is often in one file. That is fine for 50 lines. "
        "A company API has many URLs, many tables, and many people. If everything is in one file, "
        "it becomes hard to find a bug and hard to add a new feature."
    ))
    story.append(p(
        "The common rule is: <b>one job per folder</b>."
    ))
    story.append(table(
        ["Layer", "Folder", "Job", "Company reason"],
        [
            ["App start", "main.py", "Create FastAPI + CORS + attach routes", "One place to start the server"],
            ["Connection", "app/database.py", "Open Postgres", "DB settings stay in one file"],
            ["Schema", "app/schemas/", "JSON shape (name, price, quantity)", "Invalid JSON is rejected early"],
            ["Service", "app/services/", "SQL with cursor", "Business work is not mixed with URLs"],
            ["Controller", "app/controllers/", "HTTP URLs", "Easy to see all APIs"],
            ["Libraries", "requirements.txt", "What pip must install", "Same versions on every machine"],
        ],
        [28 * mm, 38 * mm, 52 * mm, 52 * mm],
    ))
    story.append(spacer(3))
    story.append(p(
        "This is the same idea used in Java (controller / service / repository), "
        "in Spring Boot, in Node (routes / services), and in Python FastAPI. "
        "The names change a little. The idea does not.",
        "note",
    ))

    story.append(p("2. Project folders", "h1"))
    story.append(code_block("""
postgres-db-demo/
├── main.py                      start the app
├── requirements.txt             libraries to install
└── app/
    ├── database.py              Postgres connection
    ├── schemas/
    │   └── product.py           JSON body
    ├── services/
    │   └── product_service.py   cursor SQL (CRUD)
    └── controllers/
        └── product_controller.py  GET POST PUT DELETE URLs
"""))
    story.append(p(
        "Empty <font face='Courier'>__init__.py</font> files make a folder a Python package, "
        "so other files can write <font face='Courier'>from app.services.product_service import ProductService</font>.",
        "small",
    ))

    story.append(p("2.1  main.py  — start the application", "h2"))
    story.append(p(
        "This file does three things only: create the FastAPI app, allow the React UI (CORS), "
        "and attach the product routes. It does not contain SQL."
    ))
    story.append(code_block("""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import product_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)
"""))
    story.append(p(
        "CORS: the UI is http://localhost:5173 and the API is http://localhost:8000. "
        "Different ports mean different origins. The browser blocks the call unless the API says the UI is allowed. "
        "Swagger can work without CORS. The React UI cannot.",
        "note",
    ))

    story.append(p("2.2  app/database.py  — open PostgreSQL", "h2"))
    story.append(p(
        "Companies keep connection details in one place. If the password or database name changes, "
        "only this file is edited. <font face='Courier'>row_factory=dict_row</font> makes each row a dictionary "
        "like {\"id\": 1, \"name\": \"Mouse\"} so the UI can read field names."
    ))
    story.append(code_block("""
def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres123",
        port=5432,
        row_factory=dict_row,
    )
"""))

    story.append(p("2.3  app/schemas/  — JSON contract", "h2"))
    story.append(p(
        "A schema is not the database table. It is the JSON that the client sends. "
        "If price is text, Pydantic rejects the request before SQL runs. "
        "That is why companies separate schema from SQL."
    ))
    story.append(code_block("""
class Product(BaseModel):
    name: str
    price: float
    quantity: int
"""))

    story.append(p("2.4  app/services/  — SQL / business logic", "h2"))
    story.append(p(
        "The service talks to Postgres with a cursor. This is the same simple logic as a single-file demo: "
        "connect, execute, fetch, commit, close. The only change is: this code lives in a service class, "
        "so the controller stays small."
    ))
    story.append(code_block("""
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()
cursor.close()
conn.close()
return products
"""))
    story.append(table(
        ["Service method", "SQL idea"],
        [
            ["get_all_products", "SELECT * FROM products"],
            ["create_product", "INSERT ... RETURNING *"],
            ["update_product", "UPDATE ... WHERE id = ? RETURNING *"],
            ["delete_product", "DELETE FROM products WHERE id = ?"],
        ],
        [55 * mm, 115 * mm],
    ))

    story.append(p("2.5  app/controllers/  — HTTP routes", "h2"))
    story.append(p(
        "A controller maps a URL + method to a service method. It should not contain SQL. "
        "If the URL changes, only this file changes. If the SQL changes, only the service changes. "
        "That is how teams work in parallel."
    ))
    story.append(code_block("""
@router.get("/products")
def get_products(service: ProductService = Depends(get_product_service)):
    return service.get_all_products()
"""))
    story.append(p(
        "<font face='Courier'>Depends</font> means FastAPI creates the service for the request. "
        "This is called dependency injection. The function asks for a ProductService. It does not build it by hand.",
        "note",
    ))

    story.append(PageBreak())
    story.append(p("3. API routes", "h1"))
    story.append(p(
        "CRUD means Create, Read, Update, Delete. HTTP already has words for that."
    ))
    story.append(table(
        ["Action", "HTTP", "URL", "Controller function", "Service method"],
        [
            ["Read all", "GET", "/products", "get_products", "get_all_products"],
            ["Create", "POST", "/products", "create_product", "create_product"],
            ["Update one", "PUT", "/products/{product_id}", "update_product", "update_product"],
            ["Delete one", "DELETE", "/products/{product_id}", "delete_product", "delete_product"],
        ],
        [28 * mm, 24 * mm, 42 * mm, 38 * mm, 38 * mm],
    ))
    story.append(spacer(3))
    story.append(p("Sample JSON for POST and PUT:", "body"))
    story.append(code_block("""
{
  "name": "Wireless Mouse",
  "price": 799,
  "quantity": 25
}
"""))
    story.append(p("How one POST request travels:", "h2"))
    story.append(code_block("""
Browser / UI
   POST http://localhost:8000/products
        |
        v
Controller   receives URL and JSON
        |
        v
Schema       checks name, price, quantity
        |
        v
Service      INSERT with cursor, commit
        |
        v
PostgreSQL   new row, id is generated
        |
        v
JSON back to the UI
"""))

    story.append(p("4. requirements.txt  — how companies install libraries", "h1"))
    story.append(p(
        "Python projects do not assume every machine already has FastAPI. "
        "Companies list libraries in requirements.txt. Anyone can recreate the same environment with pip."
    ))
    story.append(code_block("""
fastapi          # write APIs
uvicorn          # run the server
psycopg[binary]  # talk to PostgreSQL
pydantic         # validate JSON
"""))
    story.append(p(
        "Why not install packages by hand each time? Because one person may have FastAPI 0.100 and another 0.115. "
        "A shared requirements file keeps the team aligned. In larger companies this file is also used in CI servers "
        "and Docker images so production matches the laptop.",
        "note",
    ))
    story.append(p("Create a virtual environment first, so project libraries do not mix with system Python:", "body"))
    story.append(code_block("""
cd postgres-db-demo
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
"""))

    story.append(p("4.1  Why these two commands: venv and activate", "h2"))
    story.append(p(
        "Those two commands create a <b>private Python</b> for this project, then <b>switch to it</b>."
    ))
    story.append(p("<b>1. python3 -m venv .venv</b>", "h2"))
    story.append(p(
        "Creates a folder named <font face='Courier'>.venv</font> with its own Python and pip. "
        "Without this, <font face='Courier'>pip install fastapi</font> goes into the system Python. Then one project "
        "may need FastAPI 0.100 and another 0.115. Packages mix and break. "
        "<font face='Courier'>.venv</font> is this project's own toolbox."
    ))
    story.append(p("<b>2. source .venv/bin/activate</b>", "h2"))
    story.append(p(
        "Turns that toolbox on in the current terminal. After activate, <font face='Courier'>python</font> and "
        "<font face='Courier'>pip</font> mean this project's Python, not the global one. "
        "The prompt usually shows <font face='Courier'>(.venv)</font>."
    ))
    story.append(p("Windows:", "body"))
    story.append(code_block("""
.venv\\Scripts\\activate
"""))
    story.append(code_block("""
Laptop Python                 <- do not dump project libraries here
   |
   +-- .venv                  <- only for postgres-db-demo
         fastapi
         uvicorn
         psycopg
"""))
    story.append(callout(
        "One sentence",
        "venv creates a clean Python for this app. activate tells the terminal to use it. "
        "Then pip install -r requirements.txt installs libraries into .venv only. "
        "After the terminal is closed, run activate again before uvicorn. To leave it: deactivate.",
    ))
    story.append(p(
        "Create .venv only once per project. Activate it every time a new terminal is opened.",
        "note",
    ))

    story.append(p("5. How to run the app", "h1"))
    story.append(p("<b>Before start</b>", "h2"))
    story.append(bullets([
        "PostgreSQL is running",
        "A table named products exists (id, name, price, quantity)",
        "app/database.py has the correct username, password, and database name",
    ]))
    story.append(p("<b>Start the API</b>", "h2"))
    story.append(code_block("""
cd postgres-db-demo
source .venv/bin/activate
uvicorn main:app --reload
"""))
    story.append(p(
        "<font face='Courier'>main:app</font> means: file main.py, variable app. "
        "<font face='Courier'>--reload</font> restarts the server when a Python file is saved."
    ))
    story.append(table(
        ["What", "URL"],
        [
            ["API home / docs", "http://localhost:8000/docs"],
            ["List products", "http://localhost:8000/products"],
            ["React UI (if used)", "http://localhost:5173"],
        ],
        [70 * mm, 100 * mm],
    ))
    story.append(spacer(3))
    story.append(p("Test in Swagger in this order: GET /products, POST /products, PUT /products/{id}, DELETE /products/{id}.", "body"))

    story.append(p("6. If something fails", "h1"))
    story.append(table(
        ["Problem", "Likely cause", "Fix"],
        [
            ["ModuleNotFoundError: app", "Wrong folder", "cd into postgres-db-demo, then run uvicorn"],
            ["password authentication failed", "Wrong DB password", "Edit app/database.py"],
            ["relation products does not exist", "Table not created", "CREATE TABLE in pgAdmin"],
            ["UI cannot load products", "CORS or API not running", "Start uvicorn, keep CORS for port 5173"],
            ["npm / node not found", "Node.js missing (UI only)", "Install Node.js LTS from nodejs.org"],
            ["pip installs into Anaconda / system", "Forgot activate", "source .venv/bin/activate, then pip install"],
        ],
        [52 * mm, 52 * mm, 66 * mm],
    ))

    story.append(p("7. Four lines to remember", "h1"))
    story.append(code_block("""
Controller = URL
Schema     = JSON
Service    = SQL (cursor)
database.py = Postgres connection

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
http://localhost:8000/docs
"""))
    story.append(spacer(3))
    story.append(callout(
        "What companies add later (not required in this demo)",
        "Alembic migrations, .env for passwords, tests, Docker, login/auth, logging. "
        "The folder idea stays the same when those are added.",
    ))

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=22 * mm,
        bottomMargin=18 * mm,
        title="FastAPI Product API — Folder Guide",
        author="Backend Course Notes",
    )
    doc.build(story, onFirstPage=cover_page, onLaterPages=header_footer)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
