import React from "react";
import { Box, Paper, Typography } from "@mui/material";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip as ChartTooltip,
  ResponsiveContainer,
} from "recharts";

const FunctionLengthChart = ({ analytics }) => {
  if (!analytics?.functionLengths?.length) return null;
  const data = analytics.functionLengths.map((len, index) => ({
    name: `func ${index + 1}`,
    length: len,
  }));

  return (
    <Paper sx={{ p: 2, mt: 4 }}>
      <Box my={4}>
        <Typography variant="h6" gutterBottom>
          Function Lengths
        </Typography>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <XAxis dataKey="name" />
            <YAxis />
            <ChartTooltip />
            <Bar dataKey="length" fill="#66bb6a" />
          </BarChart>
        </ResponsiveContainer>
      </Box>
    </Paper>
  );
};

export default FunctionLengthChart;
