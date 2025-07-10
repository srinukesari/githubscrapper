// src/analytics/CodeSmellChart.jsx
import React, { useState } from "react";
import { Typography, Box, Chip, Paper, Button } from "@mui/material";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  LabelList,
} from "recharts";
import ComplexityLegendDialog from "./ComplexityLegendDialog";

const CodeSmellChart = ({ smells }) => {
  if (!smells || !smells.functions?.length) return null;

  const { functions, maintainability_index } = smells;

  const [legendOpen, setLegendOpen] = useState(false);

  return (
    <Paper sx={{ p: 2, mt: 4 }}>
      <Typography variant="h6" gutterBottom>
        Code Smell Analysis
      </Typography>

      <Box
        display="flex"
        alignItems="space-between"
        justifyContent="space-between"
        gap={2}
        mb={2}>
        <Chip
          label={`Maintainability Index: ${maintainability_index.score.toFixed(
            1
          )} (${maintainability_index.rank})`}
          color={
            maintainability_index.rank === "A"
              ? "success"
              : maintainability_index.rank === "F"
              ? "error"
              : "warning"
          }
          variant="outlined"
        />
        <Button
          variant="filled"
          size="small"
          sx={{ mb: 2, color: "primary" }}
          onClick={() => setLegendOpen(true)}>
          What does this mean?
        </Button>
      </Box>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={functions}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="complexity" fill="#8884d8">
            <LabelList dataKey="rank" position="top" />
          </Bar>
        </BarChart>
      </ResponsiveContainer>

      <ComplexityLegendDialog
        open={legendOpen}
        handleClose={() => setLegendOpen(false)}
      />
    </Paper>
  );
};

export default CodeSmellChart;
