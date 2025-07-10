// src/analytics/ComplexityLegendDialog.jsx
import React from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  IconButton,
  Typography,
  Divider,
  Chip,
  Stack,
  Box,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";

const ComplexityLegendDialog = ({ open, handleClose }) => {
  return (
    <Dialog open={open} onClose={handleClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ m: 0, p: 2 }}>
        Complexity & Rank Guide
        <IconButton
          aria-label="close"
          onClick={handleClose}
          sx={{
            position: "absolute",
            right: 8,
            top: 8,
            color: "grey.500",
          }}>
          <CloseIcon />
        </IconButton>
      </DialogTitle>

      <DialogContent dividers>
        <Typography variant="body2" gutterBottom>
          Cyclomatic Complexity measures how many independent paths your code
          has. Higher values mean more branches and harder-to-maintain code.
        </Typography>

        <Divider sx={{ my: 2 }} />

        <Typography variant="subtitle2" gutterBottom>
          Complexity Scores
        </Typography>
        <Stack direction="column" spacing={0.5} mb={2}>
          <Typography variant="body2">1 to 5 - Simple logic</Typography>
          <Typography variant="body2">6 to 10 - Moderate logic</Typography>
          <Typography variant="body2">
            11+ - Complex, needs refactoring
          </Typography>
        </Stack>

        <Divider sx={{ my: 2 }} />

        <Typography variant="subtitle2" gutterBottom>
          Rank Scale
        </Typography>
        <Stack direction="row" spacing={2} flexWrap="wrap">
          <Chip label="A (1 - 5) Excellent" color="success" sx={{ m: 20 }} />
          <Chip label="B (6 - 10) Good" color="info" />
          <Chip label="C (11 - 20) OK" color="warning" />
          <Chip label="D (21 - 30) Bad" color="error" />
          <Chip label="E (31 - 40) Very Bad" color="error" variant="outlined" />
          <Chip
            label="F (>40) Unmaintainable"
            color="error"
            variant="outlined"
            sx={{ m: 20 }}
          />
        </Stack>
      </DialogContent>
    </Dialog>
  );
};

export default ComplexityLegendDialog;
