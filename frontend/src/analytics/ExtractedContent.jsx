import React, { useState } from "react";
import { Paper, Box, Chip, IconButton, Tooltip } from "@mui/material";
import ContentCopyIcon from "@mui/icons-material/ContentCopy";
import LibraryAddCheckIcon from "@mui/icons-material/LibraryAddCheck";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import vs from "react-syntax-highlighter/dist/esm/styles/prism/vs";

const ExtractedContent = ({ language, content, copied, setCopied }) => {
  const handleCopy = () => {
    if (!content) return;
    navigator.clipboard.writeText(content).then(() => {
      setCopied(true);
      //   setTimeout(() => setCopied(false), 2000);
    });
  };

  return (
    <Paper
      elevation={3}
      sx={{
        padding: 2,
        backgroundColor: "#f5f5f5",
        mb: 4,
      }}>
      <Box
        display="flex"
        justifyContent="space-between"
        alignItems="center"
        mb={1}>
        <Chip
          label={`${language}`}
          color="success"
          variant="default"
          size="medium"
          sx={{ fontWeight: 800 }}
        />
        <Tooltip title={copied ? "Copied!" : "Copy to clipboard"}>
          <IconButton
            size="small"
            onClick={handleCopy}
            sx={{ color: copied ? "success.main" : "text.primary" }}>
            {copied ? <LibraryAddCheckIcon /> : <ContentCopyIcon />}
          </IconButton>
        </Tooltip>
      </Box>

      <Box
        sx={{
          maxHeight: "60vh",
          overflow: "auto",
        }}>
        <SyntaxHighlighter
          language="jsx"
          style={vs}
          showLineNumbers
          customStyle={{ margin: 0, background: "transparent" }} // Optional: for tighter look
        >
          {content}
        </SyntaxHighlighter>
      </Box>
    </Paper>
  );
};

export default ExtractedContent;
