import LandingShowCase from "../../recycle/LandingShowCase";
import HookInfoText from "../../recycle/expeditionTemplate/HookInfoText";
import PackageInfoNavigation from "../../recycle/expeditionTemplate/PackageInfoNavigation";
import { Fragment, useEffect, useState } from "react";
import ExpeditionInfo from "../../recycle/expeditionTemplate/ExpeditionInfo";
import Gallery from "../../recycle/expeditionTemplate/Gallary";
import PricingInfo from "../../recycle/expeditionTemplate/PricingInfo";
import ItineraryInfo from "../../recycle/expeditionTemplate/ItineraryInfo";
import PackageInclusion from "../../recycle/expeditionTemplate/PackageInclusion";
import CancellationDetails from "../../recycle/expeditionTemplate/CancellationDetails";
import { useParams } from "react-router-dom";
//redux
import { useDispatch, useSelector } from "react-redux";
import { selectStatus, selectTrekPackage, getTrekPackage, resetStatus } from "./trekSlice";
import { ExpeditionObject } from "../../recycle/ExpeditionObject";
import { IParams } from "./types.d";

export default function TrekExpedition() {
    const { id }: IParams = useParams();
    const dispatch = useDispatch();
    const status = useSelector(selectStatus);
    const trekPackage = useSelector(selectTrekPackage);

    useEffect(() => {
        if (status === 'idel') dispatch(getTrekPackage(id));
    }, [status]);

    useEffect(() => {
        if (status !== 'idel') dispatch(resetStatus());
    }, [id]);

    return (
        <Fragment>
            {trekPackage === undefined
                ? (
                    <div>Loading</div>
                ) : (
                    <Fragment>
                        <LandingShowCase />
                        <HookInfoText hook={trekPackage.hook} />
                        <PackageInfoNavigation />
                        <ExpeditionInfo expedition_info={trekPackage.expedition_info} />
                        {/* <Gallery /> */}
                        <PricingInfo pricing_info={trekPackage.pricing_info} />
                        <ItineraryInfo itinerary_info={trekPackage.itinerary_info} />
                        {/* PackageInclusion Needs to be updated */}
                        <PackageInclusion packageInclusion={ExpeditionObject.packageInclusion} />
                        <CancellationDetails />
                    </Fragment>
                )
            }
        </Fragment>
    );
}
