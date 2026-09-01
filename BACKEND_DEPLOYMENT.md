╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                  🌐 BACKEND DEPLOYMENT - STEP 2                           ║
║                                                                            ║
║          SIH26006 Freight Forecasting | Sept 1, 2026 - 5:40 PM           ║
║                  Deploy Flask API with Trained Model                      ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝


✅ PREVIOUS STEP COMPLETE
────────────────────────────────────────────────────────────────────────────
ML Model: ✅ TRAINED (86.1% accuracy)
File: xgboost_model.pkl (1.2 MB) - Saved in project folder


⏭️ CURRENT STEP: DEPLOY BACKEND API
────────────────────────────────────────────────────────────────────────────
WHO: Backend Developer
WHERE: Replit.com (same place as model training)
TIME: 15-20 minutes
GOAL: Live API endpoint at /api/predict


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 STEP-BY-STEP DEPLOYMENT (20 minutes)
────────────────────────────────────────────────────────────────────────────

OPTION A: REPLIT DEPLOYMENT (Recommended - No Local Setup)
═══════════════════════════════════════════════════════════

1️⃣ CREATE NEW PYTHON REPL (1 minute)
   └─ Go to: https://replit.com
   └─ Click: "+ Create"
   └─ Choose: Python
   └─ Click: "Create Repl"

2️⃣ UPLOAD FILES (2 minutes)
   └─ Click: "Upload files"
   └─ Upload from C:\Users\thont\Desktop\sairam-ai\:
      ├─ app.py ← MAIN FILE
      ├─ xgboost_model.pkl ← TRAINED MODEL
      └─ requirements.txt (create new file with this content):

         flask
         scikit-learn
         xgboost
         pandas
         numpy

3️⃣ INSTALL DEPENDENCIES (2 minutes)
   └─ Click: "Shell" tab
   └─ Type: pip install -r requirements.txt
   └─ Press: Enter
   └─ Wait for installation

4️⃣ RUN FLASK APP (1 minute)
   └─ In Shell, type: python app.py
   └─ Press: Enter
   └─ You'll see:
   
      🚀 SAIL FREIGHT FORECASTING DASHBOARD
      ════════════════════════════════════════
         🌐 Running on: http://localhost:5000
         📊 Accuracy: 86.1%
         💡 Press Ctrl+C to stop

5️⃣ GET PUBLIC URL (1 minute)
   └─ Look at top of Replit window
   └─ You'll see: [ProjectName].repl.co
   └─ This is your PUBLIC API URL
   └─ Example: https://freight-forecasting.repl.co

6️⃣ OPEN IN BROWSER (1 minute)
   └─ Click the URL or open in new tab
   └─ You should see:
      ├─ SAIL logo
      ├─ 4 stat boxes (Accuracy, Savings, Data Points, Speed)
      ├─ Input form
      └─ "Get AI Recommendation" button

7️⃣ TEST THE API (2 minutes)
   └─ In the form, enter:
      ├─ Volume: 10000
      ├─ Rate: 10.80
      ├─ Coal: 115
      ├─ Oil: 78
      ├─ Month: August
   └─ Click: "Get AI Recommendation"
   └─ Should see:
      ├─ Chart updates
      ├─ Recommendation appears
      ├─ Savings displayed
   └─ ✅ API WORKING!

8️⃣ SHARE WITH TEAM (1 minute)
   └─ Copy the public URL
   └─ Send to Frontend person:
      "Backend is live! API at: https://[your-repl].repl.co"
   └─ Send to Presentation person:
      "Demo live at: https://[your-repl].repl.co"


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OPTION B: LOCAL DEPLOYMENT (If Python works on your machine)
═════════════════════════════════════════════════════════════

1️⃣ INSTALL DEPENDENCIES
   └─ Open Command Prompt
   └─ cd C:\Users\thont\Desktop\sairam-ai
   └─ pip install flask scikit-learn xgboost pandas numpy

2️⃣ RUN FLASK APP
   └─ python app.py
   └─ Server runs at: http://localhost:5000

3️⃣ TEST IN BROWSER
   └─ Open: http://localhost:5000
   └─ Fill form and test

4️⃣ SHARE FOR DEMO
   └─ Keep terminal running
   └─ Tell others: "API at localhost:5000"
   └─ Frontend person connects to it


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 WHAT THE API DOES
────────────────────────────────────────────────────────────────────────────

GET /
  └─ Shows interactive dashboard
  └─ Beautiful UI with form
  └─ Works in any browser

POST /api/predict
  └─ Input:
     {
       "current_rate": 10.80,
       "volume": 10000,
       "month": 8,
       "coal_price": 115,
       "oil_price": 78
     }
  
  └─ Output:
     {
       "current_rate": 10.80,
       "predicted_rate": 10.50,
       "recommendation": "WAIT",
       "savings": 10200,
       "confidence": "86.1%"
     }


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ VERIFICATION CHECKLIST
────────────────────────────────────────────────────────────────────────────

After deployment:

☐ API is running (shows "Running on...")
☐ Can open dashboard in browser
☐ Form inputs work (can enter values)
☐ "Get AI Recommendation" button works
☐ Chart displays (line graph with 4 weeks)
☐ Recommendation appears (WAIT or CHARTER NOW)
☐ Savings calculation shows
☐ Can refresh page without errors

If all checked: ✅ BACKEND READY!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🆘 TROUBLESHOOTING
────────────────────────────────────────────────────────────────────────────

PROBLEM: "ModuleNotFoundError: No module named 'flask'"
SOLUTION: Run: pip install flask

PROBLEM: "Can't find xgboost_model.pkl"
SOLUTION:
  1. Make sure you uploaded the pkl file to Replit
  2. Check Files tab on left
  3. Verify filename is exactly: xgboost_model.pkl

PROBLEM: "Port 5000 already in use"
SOLUTION:
  1. Replit automatically handles this
  2. Or change port in app.py: app.run(port=5001)

PROBLEM: "Replit app crashes when I click button"
SOLUTION:
  1. Check console for error message
  2. Usually means xgboost_model.pkl not loaded
  3. Make sure file was uploaded

PROBLEM: "API works but predictions look wrong"
SOLUTION:
  1. That's normal - predictions are based on model
  2. Predictions should change as inputs change
  3. If not changing, check JavaScript console

PROBLEM: "Can't access Replit URL from outside"
SOLUTION:
  1. Make sure Replit project is public (not private)
  2. Check project settings
  3. Share link is at top of window


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 FILES YOU NEED
────────────────────────────────────────────────────────────────────────────

Upload to Replit:
  ├─ app.py (Flask backend with routes)
  ├─ xgboost_model.pkl (trained model - 1.2 MB)
  └─ requirements.txt (dependencies)

Create requirements.txt with:
  flask
  scikit-learn
  xgboost
  pandas
  numpy


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ TIMELINE
────────────────────────────────────────────────────────────────────────────

Setup Replit:              1 min
Upload files:             2 min
Install packages:         2 min
Run Flask:                1 min
Test API:                 2 min
Share URL:                1 min
──────────────────────────────
TOTAL:                     9 min
(Can do in parallel with frontend work)


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📞 WHAT TO TELL OTHER TEAM MEMBERS
────────────────────────────────────────────────────────────────────────────

TO FRONTEND PERSON:
  "Backend is live! API endpoint: https://[your-url].repl.co/api/predict
   You can now connect the dashboard to this URL"

TO PRESENTATION PERSON:
  "Full system is live for demos at: https://[your-url].repl.co
   Try it out and record the demo video!"

TO ML PERSON:
  "Model is working great! 86.1% accuracy verified in API"


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 NEXT STEP (SEPT 3)
────────────────────────────────────────────────────────────────────────────

After backend is deployed:

FRONTEND PERSON:
  └─ Connects dashboard to API
  └─ Shows live predictions
  └─ Tests all features

RESULT BY END OF SEPT 3:
  └─ ML model: ✅ trained
  └─ Backend API: ✅ deployed
  └─ Frontend dashboard: ✅ connected
  └─ Full system: ✅ working end-to-end


════════════════════════════════════════════════════════════════════════════

                  👉 START BACKEND DEPLOYMENT NOW

         Go to: https://replit.com | Time: 20 minutes
        Result: Live API endpoint ready for frontend
      Next step: Frontend connects to API (Sept 3)

════════════════════════════════════════════════════════════════════════════
