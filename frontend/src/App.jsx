import { useState } from "react";
import {
  Container,
  TextField,
  Button,
  Typography,
  Box,
  Alert,
  CircularProgress,
  Divider,
} from "@mui/material";
import axios from "axios";
import CodeSmellChart from "./analytics/CodeSmellChart";
import KeywordChart from "./analytics/KeywordChart";
import LinesofCodePieChart from "./analytics/LinesofCodePieChart";
import ExtractedContent from "./analytics/ExtractedContent";

function App() {
  const [url, setUrl] = useState("");
  const [content, setContent] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [analytics, setAnalytics] = useState(null);
  const [language, setLanguage] = useState("");
  const [copied, setCopied] = useState(false);

  const BASE_URL = import.meta.env.VITE_BASE_URL;
  const handleScrape = async () => {
    setError("");
    setContent("");
    setCopied(false);
    setAnalytics(null);
    setLoading(true);
    try {
      const res = await axios.get(`${BASE_URL}/scrape`, {
        params: { url },
      });
      setContent(res.data.content);
      setAnalytics(res.data.analytics);
      setLanguage(res.data.language);
    } catch (err) {
      setError(err.response?.data?.detail || "Something went wrong.");
    }
    setLoading(false);
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 5, mb: 8 }}>
      <Typography variant="h4" gutterBottom align="center">
        <Box
          sx={{
            display: "inline-flex",
            alignItems: "center",
            justifyContent: "center",
          }}>
          <img
            src="https://img.icons8.com/?size=100&id=LTV2516kZliP&format=png&color=000000"
            alt="logo"
            style={{ width: 40, height: 40, marginRight: 8 }}
          />
          github File Scraper
        </Box>
      </Typography>

      <Box display="flex" gap={2} alignItems="center" mb={3}>
        <TextField
          fullWidth
          label="github File URL"
          variant="outlined"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          disabled={loading}
        />
        <Button
          variant="contained"
          size="large"
          sx={{ height: "100%" }}
          color="success"
          onClick={handleScrape}
          disabled={loading || !url}>
          {loading ? <CircularProgress size={24} color="inherit" /> : "Scrape"}
        </Button>
      </Box>

      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      {content && analytics && (
        <>
          <Divider sx={{ my: 4 }} />
          <Box
            display="flex"
            flexDirection={{ xs: "column", md: "row" }}
            gap={3}
            mt={4}>
            <Box flex={1} sx={{ maxWidth: 700 }}>
              <ExtractedContent
                language={language}
                content={content}
                copied={copied}
                setCopied={setCopied}
              />
            </Box>

            <Box flex={1}>
              <Typography variant="h5" gutterBottom>
                📊 Analytics
              </Typography>
              <LinesofCodePieChart analytics={analytics} />
            </Box>
          </Box>
          <Divider sx={{ my: 4 }} />
          <Box display="flex" flexDirection="column" gap={3} mt={4}>
            <CodeSmellChart smells={analytics.smells} />
          </Box>
          <Box
            display="flex"
            flexDirection={{ xs: "column", md: "row" }}
            gap={3}
            mt={4}>
            <Box flex={1}>
              <KeywordChart analytics={analytics} />
            </Box>
            {/* <Box flex={1}>
              <FunctionLengthChart analytics={analytics} />
            </Box> */}
          </Box>
        </>
      )}
    </Container>
  );
}

export default App;
