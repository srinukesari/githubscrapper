import React from "react";
import { Box, Button, Paper, TextField, Typography } from "@mui/material";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip as ChartTooltip,
  ResponsiveContainer,
} from "recharts";

const KeywordChart = ({ analytics }) => {
  console.log(analytics?.keywordFrequency?.length);
  if (
    !analytics?.keywordFrequency ||
    Object.keys(analytics.keywordFrequency).length === 0
  )
    return null;
  const data = Object.entries(analytics.keywordFrequency).map(
    ([key, value]) => ({
      keyword: key,
      count: value,
    })
  );

  return (
    <Paper sx={{ p: 2, mt: 4 }}>
      <Box my={4}>
        <Typography variant="h6" gutterBottom>
          Keyword Frequency
        </Typography>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <XAxis dataKey="keyword" />
            <YAxis />
            <ChartTooltip />
            <Bar dataKey="count" fill="#1976d2" />
          </BarChart>
        </ResponsiveContainer>
      </Box>
    </Paper>
  );
};

export default KeywordChart;
