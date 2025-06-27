@app.post("/summarize")

def summarize(text: str = Form(...)):

    resp = hf.chat.completions.create(

        model="meta-llama/Llama-3.3-70B-Instruct",

        messages=[{"role": "user", "content": f"Summarize:\n{text}"}],

    )

    return {"summary": resp.choices[0].message.content}

 

@app.post("/chat")

def chat(query: str = Form(...)):

    resp = hf.chat.completions.create(

        model="meta-llama/Llama-3.3-70B-Instruct",

        messages=[{"role": "user", "content": query}],

    )

    return {"reply": resp.choices[0].message.content}

 

@app.post("/forecast")

def forecast(csv: UploadFile = File(...)):

    try:

        df = pd.read_csv(csv.file)

        if "value" not in df.columns:

            return {"error": "Uploaded CSV must contain a 'value' column."}

        X = np.arange(len(df)).reshape(-1, 1)

        y = df["value"].values

        model = LinearRegression().fit(X, y)

        future_X = np.arange(len(df), len(df) + 12).reshape(-1, 1)

        preds = model.predict(future_X)

        return {"forecast": preds.tolist()}

    except Exception as e:

        return {"error": f"Error processing file: {str(e)}"}

 

@app.post("/anomaly")

def anomaly(values: str = Form(...)):

    try:

        arr = np.array(list(map(float, values.split(","))))

        diffs = np.diff(arr)

        thresh = diffs.mean() + 2 * diffs.std()

        return {"anomalies": [i for i, d in enumerate(diffs) if abs(d) > thresh]}

    except Exception as e:

        return {"error": f"Invalid input: {str(e)}"}