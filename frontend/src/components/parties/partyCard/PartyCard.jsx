import React from "react";
import { Box } from "@chakra-ui/layout";

const PartyCard = ({ name, color }) => {
  return (
    <Box bg={color} height="90px">
      {name}
    </Box>
  );
};

export default PartyCard;
