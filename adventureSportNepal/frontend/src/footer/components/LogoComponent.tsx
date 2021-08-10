import { Grid, Typography } from '@material-ui/core';

export default function Logo() {
    return (
        <Grid item md={4} xs={12}>
            <Typography variant={'h1'} component={"div"}>
                {"logo"}
            </Typography>
        </Grid>
    )
}